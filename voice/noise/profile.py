from dataclasses import dataclass

@dataclass
class NoiseProfile:

    environment: str

    level: float

    reduction_strength: float

    whisper_model: str