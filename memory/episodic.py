from dataclasses import dataclass
from datetime import datetime

@dataclass
class Episode:

    goal: str

    plan: list

    result: str

    duration: float

    timestamp: datetime

class EpisodicMemory:

    def __init__(self):
        pass

    def save_episode(self, episode: Episode):
        pass

    def get_episodes(self):
        return []
