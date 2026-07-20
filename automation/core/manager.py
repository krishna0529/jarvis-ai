from automation.core.registry import AutomationRegistry
from automation.core.dispatcher import AutomationDispatcher
from automation.windows.apps import WindowsAppManager
from automation.windows.processes import ProcessManager
from automation.windows.keyboard import KeyboardManager
from automation.windows.mouse import MouseManager

class AutomationManager:

    def __init__(self):

        self.registry = AutomationRegistry()

        self.registry.register(
            "windows",
            WindowsAppManager()
        )

        self.registry.register(
            "process",
            ProcessManager()
        )

        self.dispatcher = AutomationDispatcher(
            self.registry
        )
        self.registry.register(
            "keyboard",
            KeyboardManager()
            )
        self.registry.register(
            "mouse",
            MouseManager()
)