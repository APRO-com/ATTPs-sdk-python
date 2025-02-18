from web3.types import (
    ChecksumAddress,
    Address,
    ENS,
)

from typing import (
    Union
)

from enum import Enum
from dataclasses import dataclass

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

@dataclass(eq=True, frozen=False)
class AgentHeader:
    version: str
    message_id: str
    source_agent_id: str
    source_agent_name: str
    target_agent_id: str
    timestamp: int
    message_type: MessageType
    priority: Priority
    ttl: int

@dataclass(eq=True, frozen=False)
class AgentSettings:
    signers: [Union[Address, ChecksumAddress, ENS, str]]
    threshold: int
    converter_address: Union[Address, ChecksumAddress, ENS, str]
    agent_header: AgentHeader

@dataclass(eq=True, frozen=False)
class Proofs:
    zk_proof: str
    merkle_proof: str
    signature_proof: str

@dataclass(eq=True, frozen=False)
class AgentMetadata:
    content_type: str
    encoding: str
    compression: str

@dataclass(eq=True, frozen=False)
class AgentMessagePayload:
    data: str
    data_hash: str
    proofs: Proofs
    meta_data: AgentMetadata

@dataclass(eq=True, frozen=True)
class AgentRegisterResults:
    hash: str
    agent_address: str

@dataclass(eq=True, frozen=True)
class AgentMessageVerifiedResults:
    hash: str
    verified_message: str

@dataclass(eq=True, frozen=True)
class _EIP1559GAS:
    max_fee: int
    max_priority_fee: int