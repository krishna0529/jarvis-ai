class PolicyEngine:

    def validate_action(self, action: str, params: dict) -> bool:
        # Prevent dangerous actions (e.g. deleting system files)
        if "delete" in action.lower():
            return False
        return True
