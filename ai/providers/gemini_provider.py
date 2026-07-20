from ai.provider import BaseProvider

class GeminiProvider(BaseProvider):

    def generate(self, prompt: str, **kwargs) -> str:
        return "Gemini generated response"
