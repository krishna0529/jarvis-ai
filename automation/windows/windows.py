# pyrefly: ignore [missing-import]
import pygetwindow as gw

from automation.core.result import AutomationResult


class WindowManager:

    def list_windows(self):
        """
        Returns all visible window titles.
        """
        try:
            titles = []

            for title in gw.getAllTitles():
                if title.strip():
                    titles.append(title)

            return AutomationResult(
                True,
                "Windows fetched successfully.",
                data=titles
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to fetch windows.",
                error=str(ex)
            )

    def get_window(self, title: str):

        windows = gw.getWindowsWithTitle(title)

        if not windows:
            return None

        return windows[0]

    def activate(self, title: str):

        try:

            window = self.get_window(title)

            if window is None:
                return AutomationResult(
                    False,
                    "Window not found."
                )

            window.activate()

            return AutomationResult(
                True,
                f"{title} activated."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to activate window.",
                error=str(ex)
            )

    def minimize(self, title: str):

        try:

            window = self.get_window(title)

            if window is None:
                return AutomationResult(
                    False,
                    "Window not found."
                )

            window.minimize()

            return AutomationResult(
                True,
                f"{title} minimized."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to minimize window.",
                error=str(ex)
            )

    def maximize(self, title: str):

        try:

            window = self.get_window(title)

            if window is None:
                return AutomationResult(
                    False,
                    "Window not found."
                )

            window.maximize()

            return AutomationResult(
                True,
                f"{title} maximized."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to maximize window.",
                error=str(ex)
            )

    def restore(self, title: str):

        try:

            window = self.get_window(title)

            if window is None:
                return AutomationResult(
                    False,
                    "Window not found."
                )

            window.restore()

            return AutomationResult(
                True,
                f"{title} restored."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to restore window.",
                error=str(ex)
            )

    def close(self, title: str):

        try:

            window = self.get_window(title)

            if window is None:
                return AutomationResult(
                    False,
                    "Window not found."
                )

            window.close()

            return AutomationResult(
                True,
                f"{title} closed."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to close window.",
                error=str(ex)
            )
