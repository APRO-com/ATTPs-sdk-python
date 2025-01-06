import pytest

from agent.agent import AgentSDK

AGENT_PROXY_ADDRESS = "0x07771A3026E60776deC8C1C61106FB9623521394"
NETWORK_RPC = "https://testnet-rpc.bitlayer.org"

AGENT_PROXY_TYPE_VERSION = "AI Agent Proxy 1.0.0"

class TestAgentSDK:
    def setup_method(self):
        self.agent = AgentSDK(endpoint_uri=NETWORK_RPC, proxy_address=AGENT_PROXY_ADDRESS)

    def test_type_and_version(self):
        type_version = self.agent.type_and_version()
        print("type version:", type_version)

        assert type_version == AGENT_PROXY_TYPE_VERSION

    def test_create_agent(self):
        print("todo")