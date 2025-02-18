AGENT_AGENT_ABI = [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
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
      "inputs": [],
      "name": "AccessForbidden",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadVerification",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidAllowedAgent",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidDataHash",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidProofData",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "UnsupportedProofMethod",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "ZeroAddress",
      "type": "error"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "agentSettingsDigest",
          "type": "bytes32"
        },
        {
          "indexed": True,
          "internalType": "bytes32",
          "name": "dataHash",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
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
          "indexed": False,
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
          "indexed": False,
          "internalType": "struct Common.Metadata",
          "name": "metadata",
          "type": "tuple"
        }
      ],
      "name": "MessageVerified",
      "type": "event"
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
      "inputs": [],
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