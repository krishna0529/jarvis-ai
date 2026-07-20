from .classifier import IntentClassifier
from .entities import EntityExtractor
from .normalizer import TextNormalizer
from .llm_parser import LLMIntentParser
from .models import IntentResult

class IntentManager:

    def __init__(self):
        self.classifier = IntentClassifier()
        self.extractor = EntityExtractor()
        self.normalizer = TextNormalizer()
        self.llm = LLMIntentParser()

    def process(self, text):

        normalized = self.normalizer.normalize(text)

        intent, confidence = self.classifier.classify(normalized)

        if confidence >= 0.80:
            return self.rule_result(normalized)
        return self.llm.parse(normalized)
    
    # pyrefly: ignore [invalid-syntax]
    