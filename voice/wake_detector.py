from difflib import SequenceMatcher

from voice.wakeword import WakeWords

class WakeDetector:

    def __init__(self):

        self.wake = WakeWords()

    def detect(self, text):

        text = text.lower()

        for word in self.wake.get():

            score = SequenceMatcher(
                None,
                text,
                word
            ).ratio()

            if score > 0.75:
                return True

            if word in text:
                return True

        return False