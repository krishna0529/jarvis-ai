# pyrefly: ignore [missing-import]
from pydantic import BaseModel

class Document(BaseModel):
    id: str
    title: str
    source: str
    content: str
    metadata: dict = {}
