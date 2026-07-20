# pyrefly: ignore [missing-import]
from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True
)

logger.add(
    "logs/jarvis.log",
    rotation="5 MB",
    retention="10 days",
    level="DEBUG"
)