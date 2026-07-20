from automation.core.result import AutomationResult


class PageManager:

    def __init__(self, page):
        self.page = page

    def open(self, url: str):

        try:

            self.page.goto(url)

            return AutomationResult(
                True,
                f"Opened {url}"
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to open page.",
                error=str(ex)
            )

    def refresh(self):

        try:

            self.page.reload()

            return AutomationResult(
                True,
                "Page refreshed."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Refresh failed.",
                error=str(ex)
            )

    def back(self):

        try:

            self.page.go_back()

            return AutomationResult(
                True,
                "Navigated back."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Back navigation failed.",
                error=str(ex)
            )

    def forward(self):

        try:

            self.page.go_forward()

            return AutomationResult(
                True,
                "Navigated forward."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Forward navigation failed.",
                error=str(ex)
            )

    def title(self):

        try:

            return AutomationResult(
                True,
                "Title fetched.",
                data=self.page.title()
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to fetch title.",
                error=str(ex)
            )

    def current_url(self):

        try:

            return AutomationResult(
                True,
                "URL fetched.",
                data=self.page.url
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to fetch URL.",
                error=str(ex)
            )

    def wait(self, milliseconds: int):

        try:

            self.page.wait_for_timeout(milliseconds)

            return AutomationResult(
                True,
                f"Waited {milliseconds} ms."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Wait failed.",
                error=str(ex)
            )

    def close(self):

        try:

            self.page.close()

            return AutomationResult(
                True,
                "Tab closed."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to close tab.",
                error=str(ex)
            )
