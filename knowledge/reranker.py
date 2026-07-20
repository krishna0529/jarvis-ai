class DocumentReranker:

    def rerank(self, query: str, retrieved_chunks: list, top_n=3) -> list:

        return retrieved_chunks[:top_n]
