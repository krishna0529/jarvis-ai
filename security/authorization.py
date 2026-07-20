class AuthorizationManager:

    def __init__(self):
        self.roles = {
            "admin": ["*"],
            "developer": ["browser", "code"],
            "viewer": ["read"],
            "guest": ["chat"]
        }

    def is_authorized(self, role: str, permission: str) -> bool:
        allowed = self.roles.get(role, [])
        return "*" in allowed or permission in allowed
