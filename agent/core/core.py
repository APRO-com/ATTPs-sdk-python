from time import sleep

from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
)

from eth_typing.networks import (
    URI
)

from web3 import (
    Web3,
)

from typing import (
    Union,
)

from agent.core.abis.manger import AGENT_MANAGER_ABI
from agent.core.abis.proxy import AGENT_PROXY_ABI

from agent.entities import (
    AgentRegisterResults,
    AgentSettings
)

class Agent:
    def __init__(
            self,
            endpoint_uri: Union[URI, str],
            proxy_address: Union[Address, ChecksumAddress, ENS]

    ):
        self.web3 = Web3(Web3.HTTPProvider(endpoint_uri))
        self.agent_proxy = self.web3.eth.contract(proxy_address, abi=AGENT_PROXY_ABI)
        self.agent_manger = None
        self.agent_factory = None
        self.accounts = None

    def _type_and_version(self) -> str:
        return self.agent_proxy.functions.typeAndVersion().call()

    def _create_and_register_agent(
            self,
            settings: AgentSettings
    ) -> AgentRegisterResults:
        return self.agent_proxy.functions.createAndRegisterAgent(settings).call()

    def _add_account(
            self,
            private_key: str,
    ) ->str:
        account = self.web3.eth.account.from_key(private_key)
        self.accounts[account.address] = account
        return account.address

