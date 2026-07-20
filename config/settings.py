import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv


load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    ASSISTANT_NAME = os.getenv("ASSISTANT_NAME")

    USER_NAME = os.getenv("USER_NAME")

    VOICE_RATE = int(os.getenv("VOICE_RATE"))

    VOICE_VOLUME = float(os.getenv("VOICE_VOLUME"))

    VOICE_LANGUAGE = os.getenv("VOICE_LANGUAGE")

    MEMORY_DB = os.getenv("MEMORY_DB")

    MODEL = os.getenv("MODEL")

settings = Settings()