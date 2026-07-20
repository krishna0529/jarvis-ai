from ai.provider import BaseProvider

class OpenAIProvider(BaseProvider):

    def generate(self, prompt: str, **kwargs) -> str:
        return "OpenAI generated response"
