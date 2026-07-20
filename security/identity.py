# pyrefly: ignore [missing-import]
from pydantic import BaseModel

class User(BaseModel):
    id: str
    name: str
    role: str = "guest"
