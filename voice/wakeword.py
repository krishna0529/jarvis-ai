import json

class WakeWords:

    def __init__(self):

        with open(
            "voice/wake_words.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.words = json.load(file)["wake_words"]

    def get(self):

        return self.words

    def add(self, word):

        self.words.append(word)

    def remove(self, word):

        if word in self.words:
            self.words.remove(word)