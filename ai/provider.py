class BaseProvider:

    def generate(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError
