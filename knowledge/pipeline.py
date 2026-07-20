from knowledge.retriever import DocumentRetriever
from knowledge.reranker import DocumentReranker

class KnowledgePipeline:

    def __init__(self, vector_store):
        self.retriever = DocumentRetriever(vector_store)
        self.reranker = DocumentReranker()

    def run(self, query: str) -> list:
        retrieved = self.retriever.retrieve(query)
        reranked = self.reranker.rerank(query, retrieved)
        return reranked
