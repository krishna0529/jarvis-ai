from dataclasses import dataclass

@dataclass
class Task:

    id: int

    action: str

    entities: dict

    status: str = "PENDING"
