from voice.language.detector import LanguageDetector
from voice.language.normalizer import TextNormalizer
from voice.language.parser import CommandParser


class LanguageManager:

    def __init__(self):
        self.detector = LanguageDetector()
        self.normalizer = TextNormalizer()
        self.parser = CommandParser()

    def process(self, text, whisper_info):

        language = self.detector.detect(whisper_info)

        normalized = self.normalizer.normalize(text)

        parsed = self.parser.parse(normalized)

        return {
            "language": language,
            "normalized_text": normalized,
            "parsed_command": parsed
        }