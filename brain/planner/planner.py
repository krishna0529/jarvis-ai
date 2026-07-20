from brain.planner.task import Task
from brain.planner.workflow import Workflow

class TaskPlanner:

    def create_plan(self, intent):

        tasks = []

        if intent.intent == "OPEN_APPLICATION":

            tasks.append(

                Task(

                    id=1,

                    action="OPEN_APPLICATION",

                    entities=intent.entities

                )

            )

        return Workflow(tasks)
