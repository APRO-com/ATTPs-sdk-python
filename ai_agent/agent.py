import logging
from typing import (
    Union,
    Optional,
)

from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
    Nonce
)

from eth_typing.networks import (
    URI
)

from ai_agent.core.core import Agent
from ai_agent.entities import  (
    AgentSettings,
    AgentMessagePayload,
    AgentRegisterResults,
    AgentMessageVerifiedResults,
)

class AgentSDK:
    logger = logging.getLogger("ai.agent.AgentSDK")
    endpoint_uri = None
    proxy_address = None

    def __init__(
            self,
            endpoint_uri: Union[URI, str],
            proxy_address: Union[Address, ChecksumAddress, ENS, str],
    ) -> None:
        self._core = Agent(endpoint_uri, proxy_address)


    def proxy_type_and_version(self) -> str:
        """
        Get the type and version of the agent.

        Args:

        Returns:
            str:  the agent type and version
        """

        return self._core._proxy_type_and_version()

    def add_account(
            self,
            private_key: str,
    ) ->str:
        """
        Add the account by private key.

        Args:
            private_key: the account private key

        Returns:
            str:  account address
        """

        return self._core._add_account(private_key)

    def accounts(self) ->[str]:
        """
        Get the accounts

        Args:

        Returns:
            [str]:  account addresses
        """

        return self._core._accounts()


    def create_and_register_agent(
            self,
            transmitter: Union[Address, ChecksumAddress, ENS, str],
            nonce: Optional[Union[Nonce, int]],
            settings: AgentSettings
    ) -> AgentRegisterResults:
        """
        Create and register the agent.

        Args:
            transmitter: the sender address of the agent.
            nonce: the nonce of the transmitter.
            settings: the agent settings

        Returns:
            AgentRegisterResults:  the agent register results
        """

        return self._core._create_and_register_agent(
            transmitter = transmitter,
            nonce = nonce,
            settings = settings)

    def verify(
            self,
            transmitter: Union[Address, ChecksumAddress, ENS, str],
            nonce: Optional[Union[Nonce, int]],
            agent_contract: Union[Address, ChecksumAddress, ENS, str],
            settings_digest: str,
            payload: AgentMessagePayload
    ) -> AgentMessageVerifiedResults:
        """
        Create and register the agent.

        Args:
            transmitter: the sender address of the agent.
            nonce: the nonce of the transmitter.
            agent_contract: contract address of the agent.
            settings_digest: the agent settings digest.
            payload: the message payload.

        Returns:
            AgentMessageVerifiedResults:  the agent message verified results
        """

        return self._core._verify(
            transmitter = transmitter,
            nonce = nonce,
            agent_contract = agent_contract,
            settings_digest = settings_digest,
            payload = payload
        )