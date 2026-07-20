from automation.core.result import AutomationResult


class ActionManager:

    def __init__(self, page):
        self.page = page

    def press_key(self, key: str):
        try:
            self.page.keyboard.press(key)

            return AutomationResult(
                True,
                f"Key '{key}' pressed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to press key.",
                error=str(ex)
            )

    def hotkey(self, *keys):
        try:
            combo = "+".join(keys)
            self.page.keyboard.press(combo)

            return AutomationResult(
                True,
                f"Hotkey '{combo}' executed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to execute hotkey.",
                error=str(ex)
            )

    def hover(self, selector: str):
        try:
            self.page.locator(selector).hover()

            return AutomationResult(
                True,
                "Hover completed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Hover failed.",
                error=str(ex)
            )

    def double_click(self, selector: str):
        try:
            self.page.locator(selector).dblclick()

            return AutomationResult(
                True,
                "Double click completed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Double click failed.",
                error=str(ex)
            )

    def right_click(self, selector: str):
        try:
            self.page.locator(selector).click(button="right")

            return AutomationResult(
                True,
                "Right click completed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Right click failed.",
                error=str(ex)
            )

    def select_option(self, selector: str, value: str):
        try:
            self.page.locator(selector).select_option(value)

            return AutomationResult(
                True,
                "Option selected."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Selection failed.",
                error=str(ex)
            )

    def check(self, selector: str):
        try:
            self.page.locator(selector).check()

            return AutomationResult(
                True,
                "Checkbox checked."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Check failed.",
                error=str(ex)
            )

    def uncheck(self, selector: str):
        try:
            self.page.locator(selector).uncheck()

            return AutomationResult(
                True,
                "Checkbox unchecked."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Uncheck failed.",
                error=str(ex)
            )

    def drag_and_drop(self, source: str, target: str):
        try:
            self.page.drag_and_drop(source, target)

            return AutomationResult(
                True,
                "Drag and drop completed."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Drag and drop failed.",
                error=str(ex)
            )

    def upload_file(self, selector: str, file_path: str):
        try:
            self.page.locator(selector).set_input_files(file_path)

            return AutomationResult(
                True,
                "File uploaded."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Upload failed.",
                error=str(ex)
            )