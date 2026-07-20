from memory.short_term import ShortTermMemory
from memory.long_term import LongTermMemory
from memory.semantic import SemanticMemory
from memory.episodic import EpisodicMemory

class MemoryManager:

    def __init__(self):

        self.short = ShortTermMemory()

        self.long = LongTermMemory()

        self.semantic = SemanticMemory()

        self.episodic = EpisodicMemory()
