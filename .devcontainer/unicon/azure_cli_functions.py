import subprocess
from typing import Optional

from config_builder import build_azure_config  # Neu: für automatischen Build der Konfiguration
from config_manager import load_profiles, save_profiles


def test_azure_connection() -> None:
    """Runs the command 'az account list' directly in the console."""
    subprocess.run("az account list", shell=True, check=True)


def create_profile(profile_name: str, subscription_id: str, tenant_id: str) -> None:
    """Creates an Azure profile in the JSON file."""
    profiles = load_profiles("azure")
    if profile_name in profiles:
        print(f"Profile '{profile_name}' already exists.")
        return
    profiles[profile_name] = {"subscription_id": subscription_id, "tenant_id": tenant_id}
    save_profiles("azure", profiles)
    build_azure_config()  # Update configurations
    print(f"Profile '{profile_name}' created successfully.")


def update_profile(
    profile_name: str,
    new_name: Optional[str] = None,
    subscription_id: Optional[str] = None,
    tenant_id: Optional[str] = None,
) -> None:
    """Updates an existing Azure profile in the JSON file."""
    profiles = load_profiles("azure")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return
    profile_data = profiles[profile_name]
    if subscription_id:
        profile_data["subscription_id"] = subscription_id
    if tenant_id:
        profile_data["tenant_id"] = tenant_id
    if new_name:
        profiles[new_name] = profiles.pop(profile_name)
    save_profiles("azure", profiles)
    build_azure_config()  # Update configurations
    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name: str) -> None:
    """Deletes an Azure profile from the JSON file."""
    profiles = load_profiles("azure")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return
    del profiles[profile_name]
    save_profiles("azure", profiles)
    build_azure_config()  # Update configurations
    print(f"Profile '{profile_name}' deleted successfully.")


def list_profiles() -> None:
    """Lists all Azure profiles from the JSON file."""
    profiles = load_profiles("azure")
    if profiles:
        for name, details in profiles.items():
            print(f"- {name}: Subscription ID: {details['subscription_id']}")
    else:
        print("No Azure profiles found.")


def azure_cli(action: str) -> None:
    """Handles Azure-specific CLI operations."""
    if action == "create_profile":
        profile_name = input("Enter profile name: ").strip()
        subscription_id = input(
            "Enter Azure Subscription ID.\n"
            "You can find this in the Azure portal under 'Subscriptions'.\n"
            "Example: 12345678-90ab-cdef-1234-567890abcdef\n"
            "Subscription ID: "
        ).strip()

        tenant_id = input(
            "Enter Azure Tenant ID.\n"
            "You can find this in the Azure portal under 'Azure Active Directory' → 'Tenant ID'.\n"
            "Example: abcdef12-3456-7890-abcd-ef1234567890\n"
            "Tenant ID: "
        ).strip()

        create_profile(profile_name, subscription_id=subscription_id, tenant_id=tenant_id)
        print("Testing Profile, please wait...")
        test_azure_connection()

    elif action == "update_profile":
        profile_name = input("Enter profile name to update: ").strip()
        new_name = input("New profile name (leave blank to keep current): ").strip()
        subscription_id = input("New subscription ID (leave blank to keep current): ").strip()
        tenant_id = input("New tenant ID (leave blank to keep current): ").strip()
        update_profile(
            profile_name,
            new_name=new_name or None,
            subscription_id=subscription_id or None,
            tenant_id=tenant_id or None,
        )

    elif action == "delete_profile":
        profile_name = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)

    elif action == "list_profiles":
        list_profiles()

    else:
        print(f"Unknown Azure action: {action}")
