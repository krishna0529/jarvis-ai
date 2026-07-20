# pyrefly: ignore [missing-import]
import sounddevice as sd
# pyrefly: ignore [missing-import]
import soundfile as sf

from voice.config import *

class Microphone:

    def record(self, filename):

        print("🎤 Listening...")

        recording = sd.rec(
            int(DEFAULT_RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=DTYPE
        )

        sd.wait()

        sf.write(filename, recording, SAMPLE_RATE)

        print("✅ Recording Saved")