from memory.short_term.context import ContextMemory
from memory.long_term.repository import MemoryRepository
from memory.semantic.search import SemanticSearch


class MemoryManager:

    def __init__(self):

        self.context = ContextMemory()

        self.repository = MemoryRepository()

        self.semantic = SemanticSearch()
