from tools.registry import ToolRegistry

from tools.application.open_app import OpenApplicationTool

class ToolLoader:

    def load(self):

        registry = ToolRegistry()

        registry.register(

            OpenApplicationTool()

        )

        return registry