AGENT_MANAGER_ABI = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "proxy",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [

        ],
        "name": "AgentIsAllowed",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "AgentIsRegistered",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgent",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentConfig",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentHeaderAgentId",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentHeaderMessageId",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentHeaderMessageType",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentHeaderPriority",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentHeaderVersion",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAgentSettingProposal",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidAllowedAgent",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidCallData",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidFactoryAgent",
        "type": "error"
    },
    {
        "inputs": [

        ],
        "name": "InvalidRegisteredAgent",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "digest",
                "type": "bytes32"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "AgentAccepted",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "oldProxy",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "newProxy",
                "type": "address"
            }
        ],
        "name": "AgentProxySet",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "AgentRegistered",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "AgentRemoved",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "AgentSettingsProposed",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "digest",
                "type": "bytes32"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "AgentSettingsUpdated",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferRequested",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "acceptAgent",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "acceptAgentSettingProposal",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "acceptOwnership",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "agentProxy",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "agentVersion",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "allowedAgent",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "settingDigest",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "singer",
                "type": "address"
            }
        ],
        "name": "allowedSinger",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "changeAgentSettingProposal",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "settingDigest",
                "type": "bytes32"
            }
        ],
        "name": "getAgentConfig",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "bytes32",
                        "name": "configDigest",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "configBlockNumber",
                        "type": "uint32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    },
                    {
                        "components": [
                            {
                                "internalType": "address[]",
                                "name": "signers",
                                "type": "address[]"
                            },
                            {
                                "internalType": "uint8",
                                "name": "threshold",
                                "type": "uint8"
                            },
                            {
                                "internalType": "address",
                                "name": "converterAddress",
                                "type": "address"
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "string",
                                        "name": "version",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "messageId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentName",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "targetAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "timestamp",
                                        "type": "uint256"
                                    },
                                    {
                                        "internalType": "enum Common.MessageType",
                                        "name": "messageType",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "enum Common.Priority",
                                        "name": "priority",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "ttl",
                                        "type": "uint256"
                                    }
                                ],
                                "internalType": "struct Common.AgentHeader",
                                "name": "agentHeader",
                                "type": "tuple"
                            }
                        ],
                        "internalType": "struct Common.AgentSettings",
                        "name": "settings",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentConfig",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "getAgentConfigs",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "bytes32",
                        "name": "configDigest",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "configBlockNumber",
                        "type": "uint32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    },
                    {
                        "components": [
                            {
                                "internalType": "address[]",
                                "name": "signers",
                                "type": "address[]"
                            },
                            {
                                "internalType": "uint8",
                                "name": "threshold",
                                "type": "uint8"
                            },
                            {
                                "internalType": "address",
                                "name": "converterAddress",
                                "type": "address"
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "string",
                                        "name": "version",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "messageId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentName",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "targetAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "timestamp",
                                        "type": "uint256"
                                    },
                                    {
                                        "internalType": "enum Common.MessageType",
                                        "name": "messageType",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "enum Common.Priority",
                                        "name": "priority",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "ttl",
                                        "type": "uint256"
                                    }
                                ],
                                "internalType": "struct Common.AgentHeader",
                                "name": "agentHeader",
                                "type": "tuple"
                            }
                        ],
                        "internalType": "struct Common.AgentSettings",
                        "name": "settings",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentConfig[]",
                "name": "",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "getAgentConfigsCount",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "",
                "type": "uint64"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "agentConfigIdxStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "agentConfigIdxEnd",
                "type": "uint64"
            }
        ],
        "name": "getAgentConfigsInRange",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "bytes32",
                        "name": "configDigest",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "configBlockNumber",
                        "type": "uint32"
                    },
                    {
                        "internalType": "bool",
                        "name": "isActive",
                        "type": "bool"
                    },
                    {
                        "components": [
                            {
                                "internalType": "address[]",
                                "name": "signers",
                                "type": "address[]"
                            },
                            {
                                "internalType": "uint8",
                                "name": "threshold",
                                "type": "uint8"
                            },
                            {
                                "internalType": "address",
                                "name": "converterAddress",
                                "type": "address"
                            },
                            {
                                "components": [
                                    {
                                        "internalType": "string",
                                        "name": "version",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "messageId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "sourceAgentName",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "string",
                                        "name": "targetAgentId",
                                        "type": "string"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "timestamp",
                                        "type": "uint256"
                                    },
                                    {
                                        "internalType": "enum Common.MessageType",
                                        "name": "messageType",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "enum Common.Priority",
                                        "name": "priority",
                                        "type": "uint8"
                                    },
                                    {
                                        "internalType": "uint256",
                                        "name": "ttl",
                                        "type": "uint256"
                                    }
                                ],
                                "internalType": "struct Common.AgentHeader",
                                "name": "agentHeader",
                                "type": "tuple"
                            }
                        ],
                        "internalType": "struct Common.AgentSettings",
                        "name": "settings",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentConfig[]",
                "name": "agentConfigs",
                "type": "tuple[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "getAllAllowedAgents",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "getAllRegisteringAgents",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "getAllowedAgentsCount",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "",
                "type": "uint64"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint64",
                "name": "allowedAgentIdxStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "allowedAgentIdxEnd",
                "type": "uint64"
            }
        ],
        "name": "getAllowedAgentsInRange",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "allowedAgents",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "getRegisteringAgentsCount",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "",
                "type": "uint64"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint64",
                "name": "registeringAgentIdxStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "registeringAgentIdxEnd",
                "type": "uint64"
            }
        ],
        "name": "getRegisteringAgentsInRange",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "registeringAgents",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "messageId",
                "type": "string"
            }
        ],
        "name": "isValidMessageId",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "sourceAgentId",
                "type": "string"
            }
        ],
        "name": "isValidSourceAgentId",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "address[]",
                        "name": "signers",
                        "type": "address[]"
                    },
                    {
                        "internalType": "uint8",
                        "name": "threshold",
                        "type": "uint8"
                    },
                    {
                        "internalType": "address",
                        "name": "converterAddress",
                        "type": "address"
                    },
                    {
                        "components": [
                            {
                                "internalType": "string",
                                "name": "version",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "messageId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "sourceAgentName",
                                "type": "string"
                            },
                            {
                                "internalType": "string",
                                "name": "targetAgentId",
                                "type": "string"
                            },
                            {
                                "internalType": "uint256",
                                "name": "timestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "enum Common.MessageType",
                                "name": "messageType",
                                "type": "uint8"
                            },
                            {
                                "internalType": "enum Common.Priority",
                                "name": "priority",
                                "type": "uint8"
                            },
                            {
                                "internalType": "uint256",
                                "name": "ttl",
                                "type": "uint256"
                            }
                        ],
                        "internalType": "struct Common.AgentHeader",
                        "name": "agentHeader",
                        "type": "tuple"
                    }
                ],
                "internalType": "struct Common.AgentSettings",
                "name": "agentSettings",
                "type": "tuple"
            }
        ],
        "name": "registerAgent",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            }
        ],
        "name": "removeAgent",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "proxy",
                "type": "address"
            }
        ],
        "name": "setAgentProxy",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "settingDigest",
                "type": "bytes32"
            }
        ],
        "name": "signerThreshold",
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [

        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [

        ],
        "name": "typeAndVersion",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "agent",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "validateDataConversion",
        "outputs": [
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
