class LanguageDetector:

    def detect(self, whisper_info):

        if whisper_info.language:

            return whisper_info.language

        return "en"