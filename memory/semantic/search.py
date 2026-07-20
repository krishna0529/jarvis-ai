from memory.semantic.embeddings import model

from memory.semantic.vector_store import collection


class SemanticSearch:

    def save(self, text, doc_id):

        embedding = model.encode(

            text

        ).tolist()

        collection.add(

            ids=[doc_id],

            embeddings=[embedding],

            documents=[text]

        )

    def search(self, query):

        embedding = model.encode(

            query

        ).tolist()

        return collection.query(

            query_embeddings=[embedding],

            n_results=3

        )
