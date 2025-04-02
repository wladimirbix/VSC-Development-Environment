import subprocess

from config_builder import build_databricks_config
from config_manager import load_profiles, save_profiles


def test_databricks_connection() -> None:
    """Führt den Befehl 'databricks auth profiles' direkt in der Konsole aus."""
    subprocess.run("databricks auth profiles", shell=True, check=True)


def create_profile(profile_name: str, host: str, token: str) -> None:
    """Erstellt ein Databricks-Profil in der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("databricks")
    if profile_name in profiles:
        print(f"Profile '{profile_name}' already exists.")
        return
    profiles[profile_name] = {"host": host, "token": token}
    save_profiles("databricks", profiles)
    print(f"Profile '{profile_name}' created successfully.")


def update_profile(
    profile_name: str, new_name: str | None = None, host: str | None = None, token: str | None = None
) -> None:
    """Aktualisiert ein vorhandenes Databricks-Profil in der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("databricks")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return
    profile_data = profiles[profile_name]
    if host:
        profile_data["host"] = host
    if token:
        profile_data["token"] = token
    if new_name:
        profiles[new_name] = profiles.pop(profile_name)
    save_profiles("databricks", profiles)
    build_databricks_config()  # Konfigurationen aktualisieren
    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name: str) -> None:
    """Löscht ein Databricks-Profil aus der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("databricks")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' not found.")
        return
    del profiles[profile_name]
    save_profiles("databricks", profiles)
    build_databricks_config()  # Konfigurationen aktualisieren
    print(f"Profile '{profile_name}' deleted successfully.")


def list_profiles() -> dict[str, dict[str, str]]:
    """Liest alle Databricks-Profile aus der JSON-Datei."""
    return load_profiles("databricks")


def set_default_profile(profile_name: str) -> None:
    """Setzt das angegebene Databricks-Profil als Standard in der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("databricks")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist.")
        return
    # Alle Profile zunächst auf default False setzen
    for key in profiles:
        profiles[key]["default"] = False
    profiles[profile_name]["default"] = True
    save_profiles("databricks", profiles)
    build_databricks_config()  # Konfigurationen aktualisieren
    print(f"Profile '{profile_name}' is now set as the default.")


def databricks_cli(action: str) -> None:
    """Databricks-spezifische CLI-Operationen."""
    if action == "create_profile":
        profile_name: str = input("Enter profile name: ").strip()
        host: str = input(
            "Enter Databricks host (e.g., https://adb-1234567890.12.azuredatabricks.net).\n"
            "You can find this in your Databricks workspace URL.\n"
            "Host: "
        ).strip()

        token: str = input(
            "Enter Databricks personal access token.\n"
            "You can generate this token in Databricks under 'User Settings' → 'Access Tokens'.\n"
            "Example: dapiclient1234abcdef567890...\n"
            "Token: "
        ).strip()
        create_profile(profile_name, host=host, token=token)
        set_default_profile(profile_name)
        print("Testing Profile, please wait...")
        test_databricks_connection()

    elif action == "update_profile":
        profile_name: str = input("Enter profile name to update: ").strip()
        new_name: str | None = input("New profile name (leave blank to keep current): ").strip() or None
        host: str | None = input("New host (leave blank to keep current): ").strip() or None
        token: str | None = input("New token (leave blank to keep current): ").strip() or None
        update_profile(profile_name, new_name=new_name, host=host, token=token)

    elif action == "delete_profile":
        profile_name: str = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)

    elif action == "list_profiles":
        profiles: dict[str, dict[str, str]] = list_profiles()
        if profiles:
            for name, details in profiles.items():
                default_status: str = " (default)" if details.get("default", False) else ""
                print(f"- {name}: Host: {details['host']}{default_status}")
        else:
            print("No Databricks profiles found.")

    elif action == "set_default_profile":
        profiles: dict[str, dict[str, str]] = list_profiles()
        if not profiles:
            print("No profiles found. Please create a profile first.")
            return

        print("Available profiles:")
        for name, details in profiles.items():
            default_status: str = " (default)" if details.get("default", False) else ""
            print(f"- {name}{default_status}")

        profile_name: str = input("Enter the profile name to set as default: ").strip()
        set_default_profile(profile_name)

    else:
        print(f"Unknown Databricks action: {action}")
