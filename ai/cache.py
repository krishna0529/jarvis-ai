class AICache:

    def __init__(self):

        self.cache = {}

    def get(self, prompt_hash: str):

        return self.cache.get(prompt_hash)

    def set(self, prompt_hash: str, response: str):

        self.cache[prompt_hash] = response
