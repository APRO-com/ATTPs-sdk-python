from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
)

from typing import (
    Union
)

from enum import Enum

@dataclass(eq=True, frozen=True)
class MessageType(Enum):
    Request = 0
    Response = 1
    Event = 2

@dataclass(eq=True, frozen=True)
class Priority(Enum):
    High = 0
    Medium = 1
    Low = 2

@dataclass(eq=True, frozen=True)
class AgentHeader:
    version: str
    messageId: str
    sourceAgentId: str
    sourceAgentName: str
    targetAgentId: str
    timestamp: str
    messageType: MessageType
    priority: Priority
    ttl: int

@dataclass(eq=True, frozen=True)
class AgentSettings:
    signers: [Union[Address, ChecksumAddress, ENS]]
    threshold: int
    converterAddress: Union[Address, ChecksumAddress, ENS]


@dataclass(eq=True, frozen=True)
class AgentRegisterResults:
    hash: str
    agent_address: str
