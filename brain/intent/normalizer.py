class TextNormalizer:

    REPLACEMENTS = {
        "khol do": "open",
        "kholo": "open",
        "band karo": "close",
        "browser": "chrome",
        "google chrome": "chrome",
        "vscode": "vs code"
    }

    def normalize(self, text: str) -> str:
        text = text.lower().strip()

        for old, new in self.REPLACEMENTS.items():
            text = text.replace(old, new)

        return text