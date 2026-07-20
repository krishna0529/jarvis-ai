from brain.runtime.state import AgentState
from brain.runtime.context import RuntimeContext

class AgentRuntime:

    def __init__(self, context: RuntimeContext):
        self.context = context
        self.state = AgentState.IDLE

    def run(self, planner, executor, observer, decision):
        self.state = AgentState.PLANNING
        
        # Pseudo-code loop from Phase 6
        # while self.state not in (AgentState.SUCCESS, AgentState.FAILED):
        #     plan = planner.create(self.context)
        #     result = executor.execute(plan)
        #     observation = observer.inspect(result)
        #     self.state = decision.next_state(observation)
        #     if self.state == AgentState.REPLANNING:
        #         planner.update(self.context, observation)
        pass
