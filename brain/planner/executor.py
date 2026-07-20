from tools.manager import ToolManager

class TaskExecutor:

    def __init__(self):

        self.tools = ToolManager()

    def execute(self, workflow):

        results = []

        for task in workflow.tasks:

            result = self.tools.execute(

                task.action,

                task.entities

            )

            task.status = "DONE"

            results.append(result)

        return results
