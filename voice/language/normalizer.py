class TextNormalizer:

    def normalize(self, text):

        text = text.lower().strip()

        replacements = {
            "khol do": "open",
            "kholo": "open",
            "band karo": "close",
            "chalu karo": "start",
            "band": "close"
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        return text