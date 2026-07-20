class ContextBuilder:

    def build_context(self, conversation, memory, goal, tools, events):

        return f"Context: Goal={goal}, Tools={tools}"
