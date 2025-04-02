import json
import os

# Define paths for configuration directory and files
CONFIG_DIR = os.path.join(os.path.dirname(__file__), "config")
AZURE_JSON = os.path.join(CONFIG_DIR, "azure_profiles.json")
DATABRICKS_JSON = os.path.join(CONFIG_DIR, "databricks_profiles.json")
GIT_JSON = os.path.join(CONFIG_DIR, "git_profiles.json")

# Output file paths
AZURE_CFG = os.path.expanduser("~/.azure/config")
DATABRICKS_CFG = os.path.expanduser("~/.databrickscfg")
GIT_CFG = os.path.expanduser("~/.gitconfig")


def build_azure_config() -> None:
    """Builds the Azure configuration file from the JSON profiles."""
    if not os.path.exists(AZURE_JSON):
        print(f"Azure profiles JSON not found: {AZURE_JSON}")
        return

    with open(AZURE_JSON) as file:
        profiles = json.load(file)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(AZURE_CFG), exist_ok=True)

    with open(AZURE_CFG, "w") as file:
        for profile_name, profile_data in profiles.items():
            file.write(f"[profile {profile_name}]\n")
            file.write(f"subscription_id = {profile_data['subscription_id']}\n")
            file.write(f"tenant_id = {profile_data['tenant_id']}\n")
            file.write("\n")

    print(f"Azure configuration file created at {AZURE_CFG}")


def build_databricks_config() -> None:
    """Builds the Databricks configuration file from the JSON profiles."""
    if not os.path.exists(DATABRICKS_JSON):
        print(f"Databricks profiles JSON not found: {DATABRICKS_JSON}")
        return

    with open(DATABRICKS_JSON) as file:
        profiles = json.load(file)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(DATABRICKS_CFG), exist_ok=True)

    with open(DATABRICKS_CFG, "w") as file:
        for profile_name, profile_data in profiles.items():
            file.write(f"[{profile_name}]\n")
            file.write(f"host = {profile_data['host']}\n")
            file.write(f"token = {profile_data['token']}\n")
            file.write("\n")

    print(f"Databricks configuration file created at {DATABRICKS_CFG}")


def build_git_config() -> None:
    """Builds the Git configuration file from the JSON profiles."""
    if not os.path.exists(GIT_JSON):
        print(f"Git profiles JSON not found: {GIT_JSON}")
        return

    with open(GIT_JSON) as file:
        profiles = json.load(file)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(GIT_CFG), exist_ok=True)

    with open(GIT_CFG, "w") as file:
        for profile_name, profile_data in profiles.items():
            file.write(f'[user "{profile_name}"]\n')
            file.write(f"username = {profile_data['username']}\n")
            file.write(f"token = {profile_data['token']}\n")
            file.write("\n")

    print(f"Git configuration file created at {GIT_CFG}")


def build_all_configs() -> None:
    """Builds all configuration files for Azure, Databricks, and Git."""
    build_azure_config()
    build_databricks_config()
    build_git_config()


if __name__ == "__main__":
    build_all_configs()
