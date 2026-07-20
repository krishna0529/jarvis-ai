from brain.planner.planner import TaskPlanner
from brain.agent.executor import AgentExecutor
from brain.agent.observer import Observer
from brain.agent.evaluator import Evaluator
from brain.agent.replanner import Replanner

class JarvisAgent:

    def __init__(self):

        self.planner = TaskPlanner()

        self.executor = AgentExecutor()

        self.observer = Observer()

        self.evaluator = Evaluator()

        self.replanner = Replanner()

    def run(self, intent):

        workflow = self.planner.create_plan(intent)

        results = self.executor.execute(workflow)

        for result in results:

            observation = self.observer.observe(result)

            success = self.evaluator.evaluate(observation)

            if not success:

                workflow = self.replanner.replan(workflow)

                break

        return results
