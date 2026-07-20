from brain.planner.task import Task, ExecutionPlan

class TaskPlanner:

    def create_plan(self, goal: str, parsed_commands: list) -> ExecutionPlan:
        tasks = []
        for cmd in parsed_commands:
            action = cmd.get("action")
            target = cmd.get("target")
            
            if action == "open" and target == "github":
                tasks.append(Task(
                    name="Open GitHub",
                    tool="browser",
                    action="open",
                    parameters={"url": "https://github.com"}
                ))
            elif action == "search":
                tasks.append(Task(
                    name=f"Search {target}",
                    tool="browser",
                    action="search",
                    parameters={"query": target}
                ))
                
        return ExecutionPlan(goal=goal, tasks=tasks)
