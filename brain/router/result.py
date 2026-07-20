from dataclasses import dataclass

@dataclass
class ToolResult:

    success: bool

    message: str

    data: dict | None = None