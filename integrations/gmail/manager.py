from integrations.base import BaseConnector

class GmailConnector(BaseConnector):
    name = "gmail"

    def connect(self):
        pass

    def execute(self, action, **kwargs):
        return f"Executed Gmail action: {action}"
