from dataclasses import dataclass
from typing import Any


@dataclass
class AutomationResult:
    success: bool
    message: str
    data: Any = None
    error: str | None = None
