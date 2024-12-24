from utils.audio_handler import AudioHandler
from utils.logger import setup_logger
from core.recognizer import Recognizer
from core.terminal_executor import TerminalExecutor
from utils.command_handler import CommandHandler
from db_manager import initialize_db

def main():
    logger = setup_logger()
    logger.info("Starting TerminalVoice...")

    # Initialize database
    db_session = initialize_db()

    # Ask user for input mode
    input_mode = input("Select input mode (1: Voice, 2: Manual): ").strip()

    # Initialize components
    command_handler = CommandHandler(db_session)

    if input_mode == "1":
        logger.info("Voice input mode selected.")
        audio_handler = AudioHandler()
        recognizer = Recognizer()
        terminal_executor = TerminalExecutor(recognizer, command_handler, logger)

        # Start audio stream and terminal executor
        with audio_handler.start_stream() as audio_stream:
            recognizer.set_audio_queue(audio_handler.audio_queue)
            terminal_executor.run(audio_stream)
    elif input_mode == "2":
        logger.info("Manual input mode selected.")
        print("Type commands below. Type 'exit' to quit.")
        while True:
            command = input(">> ").strip()
            if command.lower() == "exit":
                logger.info("Exiting TerminalVoice (Manual Mode).")
                break
            command_handler.execute_command(command)
    else:
        logger.error("Invalid input mode selected. Exiting.")

if __name__ == "__main__":
    main()
