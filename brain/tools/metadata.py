from dataclasses import dataclass

@dataclass
class ToolMetadata:

    name: str

    description: str

    intents: list[str]