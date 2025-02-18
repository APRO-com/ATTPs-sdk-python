AGENT_PROXY_ABI = [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [],
      "name": "InvalidAgentFactoryOrManager",
      "type": "error"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "oldFactory",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "newFactory",
          "type": "address"
        }
      ],
      "name": "AgentFactorySet",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "oldManager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "newManager",
          "type": "address"
        }
      ],
      "name": "AgentManagerSet",
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
      "inputs": [],
      "name": "acceptOwnership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "agentFactory",
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
      "inputs": [],
      "name": "agentManager",
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
      "name": "createAndRegisterAgent",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
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
          "name": "factory",
          "type": "address"
        }
      ],
      "name": "setAgentFactory",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        }
      ],
      "name": "setAgentManager",
      "outputs": [],
      "stateMutability": "nonpayable",
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
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "typeAndVersion",
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
        },
        {
          "internalType": "bytes32",
          "name": "settingsDigest",
          "type": "bytes32"
        },
        {
          "components": [
            {
              "internalType": "bytes",
              "name": "data",
              "type": "bytes"
            },
            {
              "internalType": "bytes32",
              "name": "dataHash",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "bytes",
                  "name": "zkProof",
                  "type": "bytes"
                },
                {
                  "internalType": "bytes",
                  "name": "merkleProof",
                  "type": "bytes"
                },
                {
                  "internalType": "bytes",
                  "name": "signatureProof",
                  "type": "bytes"
                }
              ],
              "internalType": "struct Common.Proofs",
              "name": "proofs",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "string",
                  "name": "contentType",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "encoding",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "compression",
                  "type": "string"
                }
              ],
              "internalType": "struct Common.Metadata",
              "name": "metadata",
              "type": "tuple"
            }
          ],
          "internalType": "struct Common.MessagePayload",
          "name": "payload",
          "type": "tuple"
        }
      ],
      "name": "verify",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]