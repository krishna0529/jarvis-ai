class PermissionEngine:

    def __init__(self, auth_manager):
        self.auth_manager = auth_manager

    def check_permission(self, role: str, action: str) -> bool:
        return self.auth_manager.is_authorized(role, action)
