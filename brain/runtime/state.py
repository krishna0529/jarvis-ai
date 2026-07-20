from enum import Enum

class AgentState(Enum):

    IDLE = "idle"

    PLANNING = "planning"

    EXECUTING = "executing"

    OBSERVING = "observing"

    REPLANNING = "replanning"

    SUCCESS = "success"

    FAILED = "failed"
