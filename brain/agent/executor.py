from brain.planner.executor import TaskExecutor

class AgentExecutor:

    def __init__(self):

        self.executor = TaskExecutor()

    def execute(self, workflow):

        return self.executor.execute(workflow)
