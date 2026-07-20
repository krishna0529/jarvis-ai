from typing import Dict, Any


class AutomationRegistry:

    def __init__(self):
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any):
        self._services[name] = service

    def get(self, name: str):
        return self._services.get(name)

    def list_services(self):
        return list(self._services.keys())
