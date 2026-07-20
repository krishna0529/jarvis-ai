from automation.core.result import AutomationResult


class AutomationDispatcher:

    def __init__(self, registry):
        self.registry = registry

    def dispatch(self, service_name: str, action: str, *args, **kwargs):

        service = self.registry.get(service_name)

        if service is None:
            return AutomationResult(
                False,
                f"Service '{service_name}' not found."
            )

        method = getattr(service, action, None)

        if method is None:
            return AutomationResult(
                False,
                f"Action '{action}' not available."
            )

        return method(*args, **kwargs)
