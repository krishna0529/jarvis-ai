from .config import INTENTS

class IntentClassifier:

    def classify(self, text: str):

        text = text.lower()

        for intent, keywords in INTENTS.items():

            for keyword in keywords:

                if keyword in text:
                    return intent, 0.95

        return "UNKNOWN", 0.0