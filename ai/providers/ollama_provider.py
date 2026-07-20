from ai.provider import BaseProvider

class OllamaProvider(BaseProvider):

    def generate(self, prompt: str, **kwargs) -> str:
        return "Ollama generated response"
