from voice.microphone import Microphone
from voice.speaker import Speaker
from voice.device import AudioDevice

class AudioManager:

    def __init__(self):

        self.microphone = Microphone()

        self.speaker = Speaker()

    def record(self):

        self.microphone.record("data/input.wav")

    def play(self):

        self.speaker.play("data/input.wav")

    def devices(self):

        return AudioDevice.list_devices()