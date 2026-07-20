# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from typing import Dict

class IntentSchema(BaseModel):
    intent: str
    confidence: float
    entities: Dict[str, str]