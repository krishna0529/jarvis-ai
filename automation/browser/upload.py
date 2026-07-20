from automation.core.result import AutomationResult


class UploadManager:

    def __init__(self, page):

        self.page = page

    def upload(
        self,
        selector: str,
        file_path: str
    ):

        try:

            self.page.locator(selector).set_input_files(
                file_path
            )

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
