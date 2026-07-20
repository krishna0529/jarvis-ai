class SecretManager:

    def __init__(self):
        self.secrets = {}

    def get_secret(self, key: str) -> str:
        return self.secrets.get(key, "")
