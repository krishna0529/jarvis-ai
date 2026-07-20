from automation.core.result import AutomationResult

# pyrefly: ignore [missing-import]
from playwright.sync_api import TimeoutError


class WaitManager:

    def __init__(self, page):

        self.page = page

    def element(
        self,
        selector,
        timeout=30000
    ):

        try:

            self.page.locator(selector).wait_for(
                state="visible",
                timeout=timeout
            )

            return AutomationResult(
                True,
                "Element is ready."
            )

        except TimeoutError:

            return AutomationResult(
                False,
                "Element timeout."
            )

    def hidden(
        self,
        selector,
        timeout=30000
    ):

        try:

            self.page.locator(selector).wait_for(
                state="hidden",
                timeout=timeout
            )

            return AutomationResult(
                True,
                "Element hidden."
            )

        except TimeoutError:

            return AutomationResult(
                False,
                "Timeout."
            )

    def navigation(
        self,
        timeout=30000
    ):

        try:

            self.page.wait_for_load_state(
                "load",
                timeout=timeout
            )

            return AutomationResult(
                True,
                "Navigation completed."
            )

        except TimeoutError:

            return AutomationResult(
                False,
                "Navigation timeout."
            )

    def dom_ready(
        self,
        timeout=30000
    ):

        try:

            self.page.wait_for_load_state(
                "domcontentloaded",
                timeout=timeout
            )

            return AutomationResult(
                True,
                "DOM Ready."
            )

        except TimeoutError:

            return AutomationResult(
                False,
                "DOM timeout."
            )

    def network_idle(
        self,
        timeout=30000
    ):

        try:

            self.page.wait_for_load_state(
                "networkidle",
                timeout=timeout
            )

            return AutomationResult(
                True,
                "Network Idle."
            )

        except TimeoutError:

            return AutomationResult(
                False,
                "Network timeout."
            )
