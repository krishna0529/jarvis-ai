from integrations.base import BaseConnector

class GitHubConnector(BaseConnector):
    name = "github"

    def connect(self):
        pass

    def execute(self, action, **kwargs):
        return f"Executed GitHub action: {action}"
