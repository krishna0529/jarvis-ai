from automation.core.result import AutomationResult


class CookieManager:

    def __init__(self, context):

        self.context = context

    def all(self):

        try:

            cookies = self.context.cookies()

            return AutomationResult(
                True,
                "Cookies fetched.",
                data=cookies
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to fetch cookies.",
                error=str(ex)
            )

    def clear(self):

        try:

            self.context.clear_cookies()

            return AutomationResult(
                True,
                "Cookies cleared."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to clear cookies.",
                error=str(ex)
            )
