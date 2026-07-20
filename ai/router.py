from ai.providers.mock_provider import MockProvider

class ModelRouter:

    def __init__(self):

        self.default_provider = MockProvider()

    def route(self, task: str):
        # Decisions based on task type
        return self.default_provider
