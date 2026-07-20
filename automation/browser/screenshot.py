from pathlib import Path
from datetime import datetime

from automation.core.result import AutomationResult


class ScreenshotManager:

    def __init__(self, page):

        self.page = page

        self.output = Path("outputs/screenshots")

        self.output.mkdir(parents=True, exist_ok=True)

    def _filename(self):

        return datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        ) + ".png"

    def page_screenshot(self):

        try:

            path = self.output / self._filename()

            self.page.screenshot(
                path=str(path),
                full_page=True
            )

            return AutomationResult(
                True,
                "Screenshot captured.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Screenshot failed.",
                error=str(ex)
            )

    def viewport(self):

        try:

            path = self.output / self._filename()

            self.page.screenshot(
                path=str(path)
            )

            return AutomationResult(
                True,
                "Viewport captured.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Capture failed.",
                error=str(ex)
            )

    def element(self, selector):

        try:

            path = self.output / self._filename()

            self.page.locator(selector).screenshot(
                path=str(path)
            )

            return AutomationResult(
                True,
                "Element screenshot captured.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Element capture failed.",
                error=str(ex)
            )
