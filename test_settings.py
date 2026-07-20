from config.settings import settings
from config.logger import logger

logger.info("Jarvis Starting...")

print(settings.ASSISTANT_NAME)
print(settings.USER_NAME)
print(settings.MODEL)
print(settings.VOICE_LANGUAGE)