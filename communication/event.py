from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Event:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    name: str = ""

    payload: dict = field(default_factory=dict)

    source: str = ""

    timestamp: datetime = field(default_factory=datetime.utcnow)
