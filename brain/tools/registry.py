class ToolRegistry:

    def __init__(self):

        self.tools = {}

    def register(self, tool):

        for intent in tool.intents:

            self.tools[intent] = tool

    def get(self, intent):

        return self.tools.get(intent)

    def list_tools(self):

        return list(self.tools.keys())