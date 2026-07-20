from dataclasses import dataclass


@dataclass
class BrowserSession:

    browser = None

    context = None

    page = None
