from tools.manager import ToolManager

class IntentRouter:

    def __init__(self):

        self.tools = ToolManager()

    def route(self, intent_result):

        return self.tools.execute(

            intent_result.intent,

            intent_result.entities

        )