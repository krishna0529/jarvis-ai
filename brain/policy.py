class PolicyEngine:

    def requires_confirmation(self, risk):

        return risk == "HIGH"