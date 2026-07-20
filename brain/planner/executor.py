class TaskExecutor:

    def execute(self, plan):

        for task in plan.tasks:

            print(task.action)
