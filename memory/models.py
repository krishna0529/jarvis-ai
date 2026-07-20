from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class MemoryItem:

    key: str

    value: object

    category: str

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    importance: float = 0.5

    tags: list[str] = field(default_factory=list)
