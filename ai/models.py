# pyrefly: ignore [missing-import]
from pydantic import BaseModel

class AIRequest(BaseModel):
    task: str
    prompt: str

class AIResponse(BaseModel):
    text: str
    provider: str
    model: str
