from dataclasses import dataclass, field
from typing import List

@dataclass
class AgentTask:
    id: int
    action: str
    entities: dict
    status: str = "PENDING"

@dataclass
class AgentState:
    goal: str
    tasks: List[AgentTask] = field(default_factory=list)
    current_step: int = 0
    completed: bool = False
