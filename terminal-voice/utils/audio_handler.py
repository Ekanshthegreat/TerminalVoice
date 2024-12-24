import sounddevice as sd
import queue

class AudioHandler:
    def __init__(self, samplerate=16000, blocksize=8000):
        self.audio_queue = queue.Queue()
        self.samplerate = samplerate
        self.blocksize = blocksize

    def audio_callback(self, indata, frames, time, status):
        """Stream audio data into the queue."""
        if status:
            print(f"Audio Status: {status}")
        self.audio_queue.put(bytes(indata))

    def start_stream(self):
        """Start the audio stream."""
        return sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            dtype="int16",
            channels=1,
            callback=self.audio_callback,
        )
