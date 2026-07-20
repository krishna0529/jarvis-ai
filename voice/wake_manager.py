from voice.wake_detector import WakeDetector

class WakeManager:

    def __init__(self):

        self.detector = WakeDetector()

    def listen(self, text):

        if self.detector.detect(text):

            print("✅ Wake Word Detected")

            return True

        return False