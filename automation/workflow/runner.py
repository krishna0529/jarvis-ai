class WorkflowRunner:

    def __init__(self, context):

        self.context = context

    def run(self, workflow):

        for step in workflow.steps:

            print(f"Running {step.name}")

            step.action(self.context)
