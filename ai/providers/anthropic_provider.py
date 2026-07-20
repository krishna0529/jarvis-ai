from ai.provider import BaseProvider

class AnthropicProvider(BaseProvider):

    def generate(self, prompt: str, **kwargs) -> str:
        return "Anthropic generated response"
