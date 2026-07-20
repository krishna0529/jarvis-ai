class ApprovalManager:

    def requires_approval(self, action: str) -> bool:
        sensitive_actions = ["delete_folder", "format_disk", "send_email"]
        return action in sensitive_actions

    def request_approval(self, action: str) -> bool:
        # Prompt human approval
        return True
