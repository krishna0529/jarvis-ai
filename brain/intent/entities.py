# pyrefly: ignore [missing-import]
from rapidfuzz import fuzz
from .config import APPLICATIONS

class EntityExtractor:

    def extract_application(self, text: str):

        text = text.lower()

        best_match = None
        best_score = 0

        for app, aliases in APPLICATIONS.items():

            for alias in aliases:

                score = fuzz.partial_ratio(alias, text)

                if score > best_score:
                    best_score = score
                    best_match = app

        if best_score >= 80:
            return best_match

        return None