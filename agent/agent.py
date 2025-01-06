import logging
from typing import (
    Union,
)

from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
)

from eth_typing.networks import (
    URI
)

from agent.core.core import Agent
from entities import (
    AgentRegisterResults,
    AgentSettings
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


    def type_and_version(self) -> str:
        """
        Get the type and version of the agent.

        Args:

        Returns:
            str:  the agent type and version
        """

        return self._core._type_and_version()

    def create_and_register_agent(
            self,
            settings: AgentSettings
    ) -> AgentRegisterResults:
        """
        Create and register the agent.

        Args:
            Common.AgentSettings: settings the agent settings

        Returns:
            str:  the agent type and version
        """

        return self._core._create_and_register_agent(settings)

    def add_account(
            self,
            private_key: str,
    ) ->str:
        """
        Add the account by private key.

        Args:
            str: the account private key

        Returns:
            str:  account address
        """

        return self._core._add_account(private_key)