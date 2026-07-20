from knowledge.pipeline import KnowledgePipeline
from knowledge.vector_store import VectorStore

class KnowledgeManager:

    def __init__(self):
        self.vector_store = VectorStore()
        self.pipeline = KnowledgePipeline(self.vector_store)

    def ingest(self, file_path: str):
        pass

    def search(self, query: str):
        return self.pipeline.run(query)

    def answer(self, question: str):
        # Coordinates with AI gateway
        pass
