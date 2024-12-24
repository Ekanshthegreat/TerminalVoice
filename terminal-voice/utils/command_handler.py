from fuzzywuzzy import process
import os
from db_manager import Command

class CommandHandler:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_commands(self):
        """Fetch all commands from the database."""
        return [cmd.name for cmd in self.db_session.query(Command).all()]

    def match_command(self, input_command):
        """Find the best matching command from the database."""
        commands = self.get_commands()
        best_match, score = process.extractOne(input_command, commands)
        return best_match, score

    def execute_command(self, command):
        """Execute a command if it matches a known terminal command."""
        best_match, score = self.match_command(command.lower())
        if score > 0:  # Confidence threshold
            print(f"Executing: {best_match} (Confidence: {score}%)")
            if best_match == "exit":
                print("Exiting TerminalVoice.")
                exit(0)
            elif best_match.startswith("cd"):
                # Handle 'cd' command
                try:
                    target_dir = command.split(" ", 1)[1]
                    os.chdir(target_dir)
                    print(f"Changed directory to: {os.getcwd()}")
                except IndexError:
                    print("Error: No directory specified.")
                except FileNotFoundError:
                    print(f"Error: Directory not found: {target_dir}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                os.system(best_match)
        else:
            print(f"Unrecognized command: {command} (Confidence: {score}%)")
