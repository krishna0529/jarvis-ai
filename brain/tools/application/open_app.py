from tools.base.tool import BaseTool

class OpenApplicationTool(BaseTool):

    name = "Open Application"

    description = "Open installed applications"

    intents = [

        "OPEN_APPLICATION"

    ]

    def execute(self, entities):

        app = entities.get("application")

        print(f"Opening {app}")

        return {

            "status":"success",

            "application":app

        }