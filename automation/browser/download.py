from pathlib import Path
from automation.core.result import AutomationResult


class DownloadManager:

    def __init__(self, page):

        self.page = page

        self.download_dir = Path("outputs/downloads")

        self.download_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def wait_for_download(self, trigger):

        try:

            with self.page.expect_download() as download_info:

                trigger()

            download = download_info.value

            path = self.download_dir / download.suggested_filename

            download.save_as(str(path))

            return AutomationResult(
                True,
                "Download completed.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Download failed.",
                error=str(ex)
            )
