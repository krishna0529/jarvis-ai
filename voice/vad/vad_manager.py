from voice.vad.vad_engine import VoiceActivityDetector

class VADManager:

    def __init__(self):

        self.vad = VoiceActivityDetector()

    def listen(self):

        self.vad.detect()