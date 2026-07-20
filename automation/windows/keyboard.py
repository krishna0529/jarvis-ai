import pyautogui

from automation.core.result import AutomationResult


class KeyboardManager:

    def type_text(self, text: str, interval: float = 0.02):
        try:
            pyautogui.write(text, interval=interval)

            return AutomationResult(
                True,
                "Text typed successfully."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to type text.",
                error=str(ex)
            )

    def press(self, key: str):
        try:
            pyautogui.press(key)

            return AutomationResult(
                True,
                f"{key} pressed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to press key.",
                error=str(ex)
            )

    def hotkey(self, *keys):
        try:
            pyautogui.hotkey(*keys)

            return AutomationResult(
                True,
                f"Hotkey {' + '.join(keys)} executed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to execute hotkey.",
                error=str(ex)
            )
