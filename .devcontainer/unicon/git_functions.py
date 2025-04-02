import subprocess

from config_builder import build_git_config
from config_manager import load_profiles, save_profiles


def test_git_connection() -> None:
    """Führt 'git config --global --list' aus, um die gespeicherten Git-Konfigurationen zu prüfen."""
    subprocess.run("git config --global --list", shell=True, check=True)


def create_profile(profile_name: str, username: str, token: str) -> None:
    """Erstellt ein Git-Profil in der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("git")
    if profile_name in profiles:
        print(f"Profile '{profile_name}' already exists.")
        return
    profiles[profile_name] = {"username": username, "token": token}
    save_profiles("git", profiles)
    build_git_config()
    print(f"Profile '{profile_name}' created successfully.")


def update_profile(
    profile_name: str, new_name: str | None = None, username: str | None = None, token: str | None = None
) -> None:
    """Aktualisiert ein vorhandenes Git-Profil in der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("git")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist.")
        return
    if new_name:
        profiles[new_name] = profiles.pop(profile_name)
        profile_name = new_name
    profile_data = profiles[profile_name]
    if username:
        profile_data["username"] = username
    if token:
        profile_data["token"] = token
    save_profiles("git", profiles)
    build_git_config()
    print(f"Profile '{profile_name}' updated successfully.")


def delete_profile(profile_name: str) -> None:
    """Löscht ein Git-Profil aus der JSON-Datei."""
    profiles: dict[str, dict[str, str]] = load_profiles("git")
    if profile_name not in profiles:
        print(f"Profile '{profile_name}' does not exist.")
        return
    del profiles[profile_name]
    save_profiles("git", profiles)
    build_git_config()
    print(f"Profile '{profile_name}' deleted successfully.")


def list_profiles() -> None:
    """Listet alle Git-Profile aus der JSON-Datei auf."""
    profiles: dict[str, dict[str, str]] = load_profiles("git")
    if profiles:
        for name, details in profiles.items():
            print(f"- {name}: Username: {details.get('username', 'N/A')}")
    else:
        print("No Git profiles found.")


def git_cli(action: str) -> None:
    """Git-spezifische CLI-Operationen."""
    if action == "create_profile":
        profile_name: str = input("Enter profile name: ").strip()
        username: str = input("Gib deinen Git-Benutzernamen ein (z. B. 'max_mustermann'): ").strip()
        token: str = input(
            "Gib deinen Git-Token ein (du kannst deinen Token unter https://github.com/settings/tokens finden): "
        ).strip()
        create_profile(profile_name, username, token)
        print("Testing Profile, please wait...")
        test_git_connection()
    elif action == "update_profile":
        profile_name: str = input("Enter profile name to update: ").strip()
        new_name: str | None = input("New profile name (leave blank to keep current): ").strip() or None
        username: str | None = input("New username (leave blank to keep current): ").strip() or None
        token: str | None = input("New token (leave blank to keep current): ").strip() or None
        update_profile(profile_name, new_name=new_name, username=username, token=token)
    elif action == "delete_profile":
        profile_name: str = input("Enter profile name to delete: ").strip()
        delete_profile(profile_name)
    elif action == "list_profiles":
        list_profiles()
    else:
        print(f"Unknown Git action: {action}")
