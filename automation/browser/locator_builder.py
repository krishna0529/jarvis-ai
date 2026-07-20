class LocatorBuilder:

    def by_role(
        self,
        role,
        name
    ):
        return ("role", role, name)

    def by_label(
        self,
        label
    ):
        return ("label", label)

    def by_placeholder(
        self,
        placeholder
    ):
        return ("placeholder", placeholder)

    def by_text(
        self,
        text
    ):
        return ("text", text)

    def by_css(
        self,
        selector
    ):
        return ("css", selector)

    def by_xpath(
        self,
        selector
    ):
        return ("xpath", selector)
