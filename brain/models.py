from dataclasses import dataclass

@dataclass
class ReasoningResult:

    approved: bool

    risk: str

    confidence: float

    explanation: str

    action: str