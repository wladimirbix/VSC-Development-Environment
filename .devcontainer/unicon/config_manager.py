import json
import os
from typing import Dict


def get_config_file_path(profile_type: str) -> str:
    """Returns the path to the profile configuration file."""
    config_dir = ".devcontainer/unicon/config"  # Save profiles in a central config directory
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, f"{profile_type}_profiles.json")


def load_profiles(profile_type: str) -> Dict[str, Dict[str, str]]:
    """Loads profiles from the specified profile type configuration file."""
    config_path = get_config_file_path(profile_type)
    if os.path.exists(config_path):
        with open(config_path, encoding="utf-8") as file:
            return json.load(file)
    return {}


def save_profiles(profile_type: str, profiles: Dict[str, Dict[str, str]]) -> None:
    """Saves profiles to the specified profile type configuration file."""
    config_path = get_config_file_path(profile_type)
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(profiles, file, indent=4)
