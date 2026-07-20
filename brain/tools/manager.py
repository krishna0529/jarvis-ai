from tools.loader import ToolLoader

class ToolManager:

    def __init__(self):

        self.registry = ToolLoader().load()

    def execute(self, intent, entities):

        tool = self.registry.get(intent)

        if tool is None:

            raise Exception(

                f"No tool registered for {intent}"

            )

        return tool.execute(entities)