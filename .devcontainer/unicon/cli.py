import sys

from azure_cli_functions import azure_cli
from databricks_functions import databricks_cli
from git_functions import git_cli


def prompt_for_action() -> None:
    """Prompts the user to select a platform and action."""
    print("Welcome to Unicon CLI!")

    while True:  # Loop to allow restarting the process
        # Platform selection with exit option
        while True:
            platform = input("Choose a platform (databricks, azure, git) or type 'exit' to quit: ").strip().lower()

            if platform == "exit":
                print("Exiting Unicon CLI...")
                sys.exit(0)  # Exit the program
            elif platform not in ["databricks", "azure", "git"]:
                print("Invalid platform. Please choose from: databricks, azure, or git, or type 'exit' to quit.")
            else:
                break  # Valid platform selected

        # Action selection
        while True:
            if platform == "databricks":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, "
                        "list_profiles, set_default_profile) or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break  # Restart platform selection
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                    "set_default_profile",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, delete_profile, "
                        "list_profiles, set_default_profile."
                    )
                else:
                    databricks_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break

            elif platform == "azure":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, list_profiles) "
                        "or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, "
                        "delete_profile, list_profiles."
                    )
                else:
                    azure_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break

            elif platform == "git":
                action = (
                    input(
                        "Choose action (create_profile, update_profile, delete_profile, list_profiles) "
                        "or type 'back' to go back: "
                    )
                    .strip()
                    .lower()
                )
                if action == "back":
                    print("\nReturning to platform selection...\n")
                    break
                elif action not in [
                    "create_profile",
                    "update_profile",
                    "delete_profile",
                    "list_profiles",
                ]:
                    print(
                        "Invalid action. Please choose from: create_profile, update_profile, "
                        "delete_profile, list_profiles."
                    )
                else:
                    git_cli(action)
                    if action == "list_profiles":
                        print("\nWhat would you like to do next?")
                        continue
                    break

            # If an action like create, update or delete happens, return to platform selection
            if action in ["create_profile", "update_profile", "delete_profile"]:
                print("\nAction completed! Returning to platform selection...\n")
                break


def main() -> None:
    """Central CLI interface for Unicon."""
    if len(sys.argv) > 1:  # If arguments are provided, process them directly
        command = sys.argv[1]
        if command == "databricks":
            databricks_cli(sys.argv[2])  # Pass the action as a string
        elif command == "azure":
            azure_cli(sys.argv[2])
        elif command == "git":
            git_cli(sys.argv[2])
        else:
            print("Unknown command.")
            sys.exit(1)
    else:
        # Otherwise, prompt for input interactively
        prompt_for_action()


if __name__ == "__main__":
    main()
