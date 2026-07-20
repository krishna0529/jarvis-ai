from pathlib import Path
from datetime import datetime

from automation.core.result import AutomationResult


class PDFManager:

    def __init__(self, page):

        self.page = page

        self.output = Path("outputs/pdf")

        self.output.mkdir(parents=True, exist_ok=True)

    def _filename(self):

        return datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        ) + ".pdf"

    def save(self):

        try:

            path = self.output / self._filename()

            self.page.pdf(
                path=str(path),
                format="A4",
                print_background=True
            )

            return AutomationResult(
                True,
                "PDF created.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "PDF generation failed.",
                error=str(ex)
            )