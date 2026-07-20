from dataclasses import dataclass

@dataclass
class SpeakerProfile:

    user_id: str

    name: str

    embedding: list