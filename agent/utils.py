import re
import uuid

import web3
from web3 import (
    Web3
)

from typing import (
    Any,
)

from enum import Enum

def is_valid_private_key(private_key: str) -> bool:
    pattern = re.compile(r"^0x[0-9a-fA-F]{64}$")
    if pattern.match(private_key):
        if Web3.is_checksum_address(Web3().eth.account.from_key(private_key).address):
            return True
    return False

def is_valid_address(address: Any) -> bool:
    if Web3.is_address(address):
        address = web3.Web3.to_checksum_address(address)
    if not Web3.is_checksum_address(address) or address == "0x0000000000000000000000000000000000000000":
        return False
    return True

def pre_processing_address(address: Any) -> Any:
    if isinstance(address, str):
        return str(web3.Web3.to_checksum_address(address))

    return address

def is_valid_uuid_v4(uuid_str: str) -> bool:
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return uuid_obj.version == 4
    except ValueError:
        return False

def is_contract_address(w3:Web3, address: Any) -> bool:
    if Web3.is_address(address):
        address = web3.Web3.to_checksum_address(address)
    if not Web3.is_checksum_address(address):
        return False

    code = w3.eth.get_code(address)

    return code != b'0x'

def generate_uuid_v4() -> str:
    return uuid.uuid4().__str__()

def add_0x_prefix(hex_str: str) -> str:
    if not hex_str.startswith("0x"):
        return "0x" + hex_str
    return hex_str

def is_valid_hex_string(hex_str) -> bool:
    return bool(re.match(r'^[0-9a-fA-F]+$', hex_str[2:])) and hex_str.startswith("0x") and len(hex_str) >= 2


def remove_spaces(func):
    def strip_object(obj, visited=None):
        if visited is None:
            visited = set()  # Used to track already visited objects

        if isinstance(obj, str):
            return obj.strip()  # Clean up spaces in the string
        elif isinstance(obj, dict):
            # Recursively process each element in the dictionary
            return {key: strip_object(value, visited) if isinstance(value, (str, dict, list)) else value for key, value in obj.items()}
        elif isinstance(obj, list):
            # Recursively process each element in the list
            return [strip_object(item, visited) if isinstance(item, (str, dict, list)) else item for item in obj]
        elif hasattr(obj, '__dict__'):
            # Check if the object has already been processed
            if id(obj) in visited:
                return obj  # If already processed, return the object as is
            visited.add(id(obj))  # Mark as processed

            # If it's an object, process its attributes
            obj_dict = vars(obj)  # Get the object's dictionary representation
            for attr, value in obj_dict.items():
                if isinstance(value, str):
                    setattr(obj, attr, value.strip())  # Clean spaces in string-type attributes
                elif isinstance(value, (dict, list)):  # Recursively process dictionary and list types
                    setattr(obj, attr, strip_object(value, visited))
                elif isinstance(value, Enum):
                    return obj  # If it's an Enum, return the object as is
                else:
                    # If the attribute is an object, try converting it to a dictionary and recursively process
                    setattr(obj, attr, strip_object(value, visited))
            return obj
        else:
            return obj  # Return other types of objects as is

    def wrapper(*args, **kwargs):
        # Recursively process the passed arguments
        args = [strip_object(arg) for arg in args]
        kwargs = {key: strip_object(value) for key, value in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper