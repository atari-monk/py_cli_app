from typing import Optional
from cli_app.config import LOGGER_CONFIG
from shared.logger import setup_logger
from cli_app.cli_helpers import get_current_working_directory, get_help
from cli_app.command_loader import discover_folders_with_commands, load_commands
from cli_app.command_runner import execute_user_input

logger = setup_logger(__name__, LOGGER_CONFIG)

def main() -> None:
    logger.info("Welcome to the Simple CLI App! Type 'help' for commands.")
    logger.info(get_current_working_directory())

    selected_folder: Optional[str] = None

    folders = discover_folders_with_commands()
    commands = load_commands(folders)

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            logger.info("Exiting the application.")
            break

        elif user_input.lower() == "help":
            logger.info(get_help(commands, selected_folder))               
        else:
            execute_user_input(user_input, commands, selected_folder)

if __name__ == "__main__":
    main()
