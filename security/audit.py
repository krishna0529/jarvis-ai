from datetime import datetime

class AuditLogger:

    def log(self, user: str, tool: str, status: str):
        print(f"[AUDIT] {datetime.utcnow()} User: {user}, Tool: {tool}, Status: {status}")
