class RiskAnalyzer:

    HIGH_RISK = {

        "DELETE_FILES",

        "FORMAT_DISK",

        "SHUTDOWN",

        "RESTART"

    }

    def analyze(self, action):

        if action in self.HIGH_RISK:

            return "HIGH"

        return "LOW"