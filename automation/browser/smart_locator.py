from automation.core.result import AutomationResult


class SmartLocator:

    def __init__(self, page):

        self.page = page

    def click(
        self,
        role=None,
        name=None,
        label=None,
        text=None,
        placeholder=None,
        css=None,
        xpath=None
    ):

        try:

            if role:

                self.page.get_by_role(
                    role,
                    name=name
                ).click()

            elif label:

                self.page.get_by_label(
                    label
                ).click()

            elif placeholder:

                self.page.get_by_placeholder(
                    placeholder
                ).click()

            elif text:

                self.page.get_by_text(
                    text
                ).click()

            elif css:

                self.page.locator(css).click()

            elif xpath:

                self.page.locator(
                    f"xpath={xpath}"
                ).click()

            return AutomationResult(
                True,
                "Click success."
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Click failed.",
                error=str(ex)
            )
