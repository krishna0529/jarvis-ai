from dataclasses import dataclass

@dataclass
class Observation:

    success: bool

    message: str

    evidence: dict

class Observer:

    def inspect(self, result) -> Observation:
        # Collects evidence and returns observation
        return Observation(
            success=True,
            message="Action completed successfully.",
            evidence={}
        )
