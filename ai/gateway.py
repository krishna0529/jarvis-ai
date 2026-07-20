class AIGateway:

    def __init__(self, router):

        self.router = router

    def generate(self, task: str, prompt: str, **kwargs) -> str:
        provider = self.router.route(task)
        return provider.generate(prompt, **kwargs)
