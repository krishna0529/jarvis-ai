from automation.core.result import AutomationResult


class LocatorManager:

    def __init__(self, page):
        self.page = page

    def click(self, selector: str):

        try:
            self.page.locator(selector).click()

            return AutomationResult(
                True,
                f"Clicked: {selector}"
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Click failed.",
                error=str(ex)
            )

    def fill(self, selector: str, text: str):

        try:
            self.page.locator(selector).fill(text)

            return AutomationResult(
                True,
                f"Filled: {selector}"
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Fill failed.",
                error=str(ex)
            )

    def text(self, selector: str):

        try:

            value = self.page.locator(selector).text_content()

            return AutomationResult(
                True,
                "Text fetched.",
                data=value
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to fetch text.",
                error=str(ex)
            )

    def visible(self, selector: str):

        try:

            value = self.page.locator(selector).is_visible()

            return AutomationResult(
                True,
                "Visibility checked.",
                data=value
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Visibility check failed.",
                error=str(ex)
            )

    def exists(self, selector: str):

        try:

            count = self.page.locator(selector).count()

            return AutomationResult(
                True,
                "Existence checked.",
                data=count > 0
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Existence check failed.",
                error=str(ex)
            )

    def wait(self, selector: str, timeout: int = 30000):

        try:

            self.page.locator(selector).wait_for(
                timeout=timeout
            )

            return AutomationResult(
                True,
                "Element ready."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Wait failed.",
                error=str(ex)
            )
