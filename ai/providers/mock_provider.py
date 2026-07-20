from ai.provider import BaseProvider

class MockProvider(BaseProvider):

    def generate(self, prompt: str, **kwargs) -> str:
        return "Mock generated response"
