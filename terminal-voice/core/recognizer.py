import os
import json
from vosk import Model, KaldiRecognizer

class Recognizer:
    def __init__(self, model_path="models/vosk-model-en-us-0.22"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}.")
        self.recognizer = KaldiRecognizer(Model(model_path), 16000)
        self.audio_queue = None

    def set_audio_queue(self, audio_queue):
        """Set the audio queue dynamically."""
        self.audio_queue = audio_queue

    def process_audio(self):
        """Process audio from the queue and return recognized text."""
        while True:
            data = self.audio_queue.get()
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                if "text" in result:
                    return result["text"]
