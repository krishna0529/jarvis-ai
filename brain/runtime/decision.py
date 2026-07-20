from brain.runtime.state import AgentState

class DecisionEngine:

    def next_state(self, observation) -> AgentState:
        if observation.success:
            return AgentState.EXECUTING
        return AgentState.REPLANNING
