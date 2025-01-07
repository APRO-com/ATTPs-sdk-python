from web3.middleware import ExtraDataToPOAMiddleware

from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
    Nonce,
    TxReceipt
)

from web3.exceptions import (
    TransactionNotFound,
    BlockNotFound,
    ContractCustomError
)

from eth_typing.networks import (
    URI
)

from web3 import (
    Web3,
)

from typing import (
    Union, Optional, Any,
)

from agent.core.abis.manger import AGENT_MANAGER_ABI
from agent.core.abis.proxy import AGENT_PROXY_ABI
from agent.core.abis.agent import AGENT_AGENT_ABI

from agent.entities import (
    AgentSettings,
    AgentMessagePayload,
    AgentRegisterResults,
    AgentMessageVerifiedResults,
    MessageType,
    Priority,
    _EIP1559GAS
)
from agent.utils import (
    add_0x_prefix,
    is_valid_private_key,
    is_valid_address,
    is_valid_uuid_v4,
    is_contract_address,
    is_valid_hex_string,
    remove_spaces,
    pre_processing_address
)


class Agent:
    @remove_spaces
    def __init__(
            self,
            endpoint_uri: Union[URI, str],
            proxy_address: Union[Address, ChecksumAddress, ENS, str]

    ):
        if not is_valid_address(proxy_address):
            raise ValueError("invalid proxy address ", proxy_address)
        proxy_address = pre_processing_address(proxy_address)

        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri))
        self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

        self.agent_proxy = self.w3.eth.contract(proxy_address, abi=AGENT_PROXY_ABI)
        self.agent_manger = self.w3.eth.contract(self.agent_proxy.functions.agentManager().call(),
                                                 abi=AGENT_MANAGER_ABI)
        self.agent_manger_error_signatures = self.__convert_contract_error_signatures(abi=AGENT_MANAGER_ABI)
        self.agent_manger_version = self.agent_manger.functions.agentVersion().call()

        self.agent_agent_error_signatures = self.__convert_contract_error_signatures(abi=AGENT_AGENT_ABI)
        self.accounts = {}

    def _proxy_type_and_version(self) -> str:
        return self.agent_proxy.functions.typeAndVersion().call()

    @remove_spaces
    def _add_account(
            self,
            private_key: str,
    ) ->str:
        private_key = add_0x_prefix(private_key)
        if not is_valid_private_key(private_key):
            raise ValueError('Private key is not valid')

        account = self.w3.eth.account.from_key(private_key)
        self.accounts[account.address] = account
        return account.address

    def _accounts(self) ->[str]:
        accounts = []
        for account in self.accounts.values():
            accounts.append(account.address)

        return accounts

    @remove_spaces
    def _create_and_register_agent(
            self,
            transmitter: Union[Address, ChecksumAddress, ENS, str],
            nonce: Optional[Union[Nonce, int]],
            settings: AgentSettings
    ) -> AgentRegisterResults:
        if not is_valid_address(transmitter):
            raise ValueError('Transmitter is not valid')
        transmitter = pre_processing_address(transmitter)

        settings = self.__validate_agent_settings(settings)

        if nonce is None:
            nonce = self.w3.eth.get_transaction_count(transmitter)

        args = (
            (
                settings.signers,
                settings.threshold,
                settings.converter_address,
                (
                    settings.agent_header.version,
                    settings.agent_header.message_id,
                    settings.agent_header.source_agent_id,
                    settings.agent_header.source_agent_name,
                    settings.agent_header.target_agent_id,
                    settings.agent_header.timestamp,
                    int(settings.agent_header.message_type.value),
                    int(settings.agent_header.priority.value),
                    settings.agent_header.ttl
                )
            )
        )

        # build and send tx
        # The example hash is on the Bitlayer testnet.
        # tx_receipt = self.web3.eth.wait_for_transaction_receipt('0xdab796be03ab5ab4bc5a3ccdfbc1ede1a8c70f998a71e6cbaeb9b13ee88f002d')
        tx_receipt = self.__build_and_send_tx(transmitter,
                                              nonce,
                                              self.agent_proxy.functions.createAndRegisterAgent,
                                              args)

        tx_agent = None

        if tx_receipt and tx_receipt['logs']:
            for log in tx_receipt['logs']:
                if self.agent_manger.address.lower() == log['address'].lower():
                    event_data = self.agent_manger.events.AgentRegistered().process_log(log)
                    tx_agent = event_data['args']['agent']

        return AgentRegisterResults(
            hash=tx_receipt["transactionHash"].to_0x_hex(),
            agent_address=tx_agent,
        )

    @remove_spaces
    def _verify(
            self,
            transmitter: Union[Address, ChecksumAddress, ENS, str],
            nonce: Optional[Union[Nonce, int]],
            agent_contract: Union[Address, ChecksumAddress, ENS, str],
            settings_digest: str,
            payload: AgentMessagePayload
    ) -> AgentMessageVerifiedResults:
        if not is_valid_address(transmitter):
            raise ValueError('Transmitter is not valid')
        transmitter = pre_processing_address(transmitter)

        if nonce is None:
            nonce = self.w3.eth.get_transaction_count(transmitter)

        if not is_contract_address(self.w3, agent_contract):
            raise ValueError('Agent contract is not valid, should be a contract address')
        agent_contract = pre_processing_address(agent_contract)

        settings_digest = add_0x_prefix(settings_digest)
        if not is_valid_hex_string(settings_digest) or len(settings_digest) != 66:
            raise ValueError('Settings digest should be 32 bytes hex string')

        payload = self.__validate_agent_payload(payload)

        if not self.agent_manger:
            self.agent_manger = self.w3.eth.contract(self.agent_proxy.functions.agentManager().call(),
                                                     abi=AGENT_MANAGER_ABI)
        payload = (
            (
                payload.data,
                payload.data_hash,
                (
                    payload.proofs.zk_proof,
                    payload.proofs.merkle_proof,
                    payload.proofs.signature_proof
                ),
                (
                    payload.meta_data.content_type,
                    payload.meta_data.encoding,
                    payload.meta_data.compression
                )
            )
        )
        # build and send tx
        # The example hash is on the Bitlayer testnet.
        # tx_receipt = self.web3.eth.wait_for_transaction_receipt('0x03d7395803427fe851d4c1b5efedda3c2d73c23c46c77fc522c0b932afe83e80')
        tx_receipt = self.__build_and_send_tx(transmitter,
                                              nonce,
                                              self.agent_proxy.functions.verify,
                                              agent_contract,
                                              settings_digest,
                                              payload)

        verified_message = {}

        if tx_receipt and tx_receipt['logs']:
            agent_obj = self.w3.eth.contract(agent_contract, abi=AGENT_AGENT_ABI)
            for log in tx_receipt['logs']:
                if agent_contract.lower() == log['address'].lower():
                    verified_message = agent_obj.events.MessageVerified().process_log(log).args


        return AgentMessageVerifiedResults(
            hash=tx_receipt["transactionHash"].to_0x_hex(),
            verified_message=verified_message,
        )

    def __build_and_send_tx(self, transmitter, nonce, build_method, *args) -> TxReceipt:
        sender = self.accounts[transmitter]
        gas = self.__eip1559_gas()

        try:
            tx = build_method(*args).build_transaction({
                "from": sender.address,
                "nonce": nonce,
                "maxFeePerGas": gas.max_fee,
                "maxPriorityFeePerGas": gas.max_priority_fee,
            })
        except ContractCustomError as e:
            error_msg = ""
            if build_method.fn_name == 'createAndRegisterAgent':
                error_msg = self.__parse_contract_error(e.args[0], self.agent_manger_error_signatures)
            elif build_method.fn_name == 'verify':
                error_msg = self.__parse_contract_error(e.args[0], self.agent_agent_error_signatures)

            raise SystemError(f"contract custom error:{error_msg}")
        except Exception as e:
            raise SystemError(f"Unknown error:{e}")



        gas_limit = self.w3.eth.estimate_gas(tx)
        tx["gas"] = gas_limit

        signed_tx = self.w3.eth.account.sign_transaction(tx, self.accounts[transmitter].key)
        tx_receipt = {}
        try:
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        except TransactionNotFound as e:
            raise SystemError(f"Transaction not found: {e}")
        except BlockNotFound as e:
            raise SystemError(f"Block not found:{e}")
        except Exception as e:
            raise SystemError(f"Unknown error:{e}")
        return tx_receipt

    def __eip1559_gas(self) -> _EIP1559GAS :
        base_fee = self.w3.eth.get_block("latest")['baseFeePerGas']
        max_priority_fee = self.w3.eth.max_priority_fee

        return _EIP1559GAS(max_priority_fee= max_priority_fee, max_fee=base_fee + max_priority_fee)

    def __validate_agent_settings(self, settings: AgentSettings) -> AgentSettings:
        for i, address in enumerate(settings.signers):
            if not is_valid_address(address):
                raise ValueError("Invalid singer:", address)
            settings.signers[i] = pre_processing_address(address)

        if settings.threshold <= 0 or settings.threshold > len(settings.signers):
            raise ValueError("Invalid threshold:", settings.threshold)

        settings.converter_address = pre_processing_address(settings.converter_address)
        if not is_contract_address(self.w3, settings.converter_address) and settings.converter_address is not "0x0000000000000000000000000000000000000000":
            raise ValueError("Invalid converter address:", settings.converter_address)

        if settings.agent_header.version != self.agent_manger_version:
            raise ValueError("Invalid agent manger version:", settings.agent_header.version, "should ", self.agent_manger_version)

        if not settings.agent_header.message_type.name in MessageType.__members__:
            raise ValueError("Invalid agent header message type:", settings.agent_header.message_type.name)

        if not settings.agent_header.priority.name in Priority.__members__:
            raise ValueError("Invalid agent header priority type:", settings.agent_header.priority.name)

        if not is_valid_uuid_v4(settings.agent_header.message_id):
            raise ValueError("Invalid agent header message id:", settings.agent_header.message_id, "must a uuid v4")

        if not is_valid_uuid_v4(settings.agent_header.target_agent_id):
            raise ValueError("Invalid agent header target agent id:", settings.agent_header.target_agent_id, "must a uuid v4")

        if not is_valid_uuid_v4(settings.agent_header.source_agent_id):
            raise ValueError("Invalid agent header source agent id:", settings.agent_header.source_agent_id, "must a uuid v4")

        if not self.agent_manger.functions.isValidSourceAgentId(settings.agent_header.source_agent_id).call():
            raise ValueError("Duplicate agent header source agent id")

        return settings

    @staticmethod
    def __validate_agent_payload(payload: AgentMessagePayload) -> AgentMessagePayload :
        payload.proofs.zk_proof = "0x"
        payload.proofs.merkle_proof = "0x"

        payload.data = add_0x_prefix(payload.data)
        if not is_valid_hex_string(payload.data):
            raise ValueError("Invalid agent payload data:", payload.data)

        payload.data_hash = add_0x_prefix(payload.data_hash)
        if not is_valid_hex_string(payload.data_hash) and len(payload.data_hash) != 66:
            raise ValueError("Invalid agent payload hash:", payload.data_hash)

        payload.proofs.signature_proof = add_0x_prefix(payload.proofs.signature_proof)
        if not is_valid_hex_string(payload.proofs.signature_proof) and (len(payload.proofs.signature_proof)-2) % 64 != 0:
            raise ValueError("Invalid agent payload signature proof:", payload.proofs.signature_proof)

        return payload
    @staticmethod
    def __convert_contract_error_signatures(abi) -> dict[str, Any] :
        error_signatures = {}
        for error in abi:
            if error['type'] == 'error':
                error_signature = f"{error['name']}({','.join([input['type'] for input in error['inputs']])})"
                error_hash = "0x" + Web3.keccak(text=error_signature).hex()[:8]
                error_signatures[error_hash] = error['name']

        return error_signatures

    @staticmethod
    def __parse_contract_error(error_id, error_signatures) -> str:
        if error_id in error_signatures:
            return error_signatures[error_id]
        else:
            return ""
