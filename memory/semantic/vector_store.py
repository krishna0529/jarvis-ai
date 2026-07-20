# pyrefly: ignore [missing-import]
import chromadb

client = chromadb.PersistentClient(

    path="./memory/vector_db"

)

collection = client.get_or_create_collection(

    "jarvis_memory"

)
