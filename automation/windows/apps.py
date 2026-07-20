import subprocess

from automation.core.result import AutomationResult


class WindowsAppManager:

    APPS = {

        "notepad": "notepad.exe",

        "calculator": "calc.exe",

        "paint": "mspaint.exe",

        "cmd": "cmd.exe",

        "explorer": "explorer.exe"
    }

    def open(self, app_name: str):

        app = self.APPS.get(app_name.lower())

        if app is None:

            return AutomationResult(
                False,
                f"{app_name} not supported."
            )

        try:

            subprocess.Popen(app)

            return AutomationResult(
                True,
                f"{app_name} opened successfully."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to open application.",
                error=str(ex)
            )
