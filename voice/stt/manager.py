from voice.stt.whisper_engine import WhisperEngine

class SpeechManager:

    def __init__(self):

        self.engine = WhisperEngine()

    def listen(self, audio):

        return self.engine.transcribe(audio)