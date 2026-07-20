from dataclasses import dataclass

@dataclass
class WorkflowStep:

    name: str

    action: callable

    retry: int = 0

    timeout: int = 30

    continue_on_error: bool = False
