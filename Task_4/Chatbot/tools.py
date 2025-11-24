import json
import os
from typing import Dict, Any

from agents import function_tool

USER_PROFILE_PATH = "user_profile.json"

@function_tool
def read_user_profile() -> Dict[str, Any]:
    """
    Reads the user profile from user_profile.json.
    Returns an empty dictionary if the file does not exist.
    """
    if not os.path.exists(USER_PROFILE_PATH):
        return {}
    with open(USER_PROFILE_PATH, "r") as f:
        return json.load(f)

@function_tool
def update_user_profile(key: str, value: str) -> str:
    """
    Updates a specific key-value pair in the user profile and saves it to user_profile.json.
    Args:
        key: The key to update or add.
        value: The value to set for the key.
    Returns:
        A confirmation message.
    """
    profile = read_user_profile()
    profile[key] = value
    with open(USER_PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)
    return f"User profile updated: {key} = {value}"
