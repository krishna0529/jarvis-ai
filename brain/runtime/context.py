from dataclasses import dataclass, field

@dataclass
class RuntimeContext:

    goal: str

    state: dict = field(default_factory=dict)

    history: list = field(default_factory=list)

    variables: dict = field(default_factory=dict)
