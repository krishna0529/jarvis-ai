# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from typing import Dict

class IntentResult(BaseModel):
    intent: str
    confidence: float
    entities: Dict[str, str]
    original_text: str