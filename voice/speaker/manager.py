from voice.speaker.database import SpeakerDatabase
from voice.speaker.recognizer import SpeakerRecognizer

class SpeakerManager:

    def __init__(self):

        self.database = SpeakerDatabase()

        self.recognizer = SpeakerRecognizer()

    def identify(self, embedding):

        return self.recognizer.recognize(embedding)