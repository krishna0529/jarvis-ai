# pyrefly: ignore [missing-import]
from brain.reasoning.models import ReasoningResult
# pyrefly: ignore [missing-import]
from brain.reasoning.risk import RiskAnalyzer
# pyrefly: ignore [missing-import]
from brain.reasoning.validator import ActionValidator
# pyrefly: ignore [missing-import]
from brain.reasoning.confidence import ConfidenceEngine
# pyrefly: ignore [missing-import]
from brain.reasoning.decision import DecisionEngine
# pyrefly: ignore [missing-import]
from brain.reasoning.policy import PolicyEngine

class ReasoningEngine:

    def __init__(self):

        self.risk = RiskAnalyzer()

        self.validator = ActionValidator()

        self.confidence = ConfidenceEngine()

        self.decision = DecisionEngine()

        self.policy = PolicyEngine()

    def evaluate(self, action, entities, score):

        risk = self.risk.analyze(action)

        valid = self.validator.validate(action, entities)

        confidence = self.confidence.calculate(score)

        approved = self.decision.decide(risk)

        return ReasoningResult(

            approved=approved and valid,

            risk=risk,

            confidence=confidence,

            explanation="Reasoning Complete",

            action=action

        )