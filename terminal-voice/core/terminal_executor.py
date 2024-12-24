class TerminalExecutor:
    def __init__(self, recognizer, command_handler, logger):
        self.recognizer = recognizer
        self.command_handler = command_handler
        self.logger = logger

    def run(self, audio_stream):
        """Start processing audio and executing commands."""
        self.logger.info("TerminalVoice is listening for commands...")
        audio_stream.start()

        try:
            while True:
                recognized_text = self.recognizer.process_audio()
                self.logger.info(f"Recognized: {recognized_text}")
                self.command_handler.execute_command(recognized_text)
        except KeyboardInterrupt:
            self.logger.info("TerminalVoice stopped by user.")
