from dataclasses import dataclass, field

@dataclass
class Task:

    name: str

    tool: str

    action: str

    parameters: dict = field(default_factory=dict)

    retry: int = 2

@dataclass
class ExecutionPlan:

    goal: str

    tasks: list = field(default_factory=list)
