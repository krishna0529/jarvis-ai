class ConfidenceEngine:

    def calculate(self, intent_score):

        return min(intent_score, 1.0)