import pyautogui

from automation.core.result import AutomationResult


class MouseManager:

    def move(self, x: int, y: int, duration: float = 0.3):
        try:
            pyautogui.moveTo(x, y, duration=duration)

            return AutomationResult(
                True,
                f"Mouse moved to ({x}, {y})."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to move mouse.",
                error=str(ex)
            )

    def click(self):
        try:
            pyautogui.click()

            return AutomationResult(
                True,
                "Left click performed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to click.",
                error=str(ex)
            )

    def right_click(self):
        try:
            pyautogui.rightClick()

            return AutomationResult(
                True,
                "Right click performed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to perform right click.",
                error=str(ex)
            )

    def double_click(self):
        try:
            pyautogui.doubleClick()

            return AutomationResult(
                True,
                "Double click performed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to perform double click.",
                error=str(ex)
            )

    def scroll(self, amount: int):
        try:
            pyautogui.scroll(amount)

            return AutomationResult(
                True,
                "Scroll completed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to scroll.",
                error=str(ex)
            )