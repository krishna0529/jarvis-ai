# pyrefly: ignore [missing-import]
from automation import browser
from voice.noise import profile
# pyrefly: ignore [missing-import]
from playwright.sync_api import sync_playwright

from automation.browser.models import BrowserSession

from automation.browser.config import BrowserConfig
from pathlib import Path


class BrowserEngine:

    def __init__(self):

        self.playwright = None

        self.session = BrowserSession()

    def start(self):

        self.playwright = sync_playwright().start()

        browser = self.playwright.chromium.launch(

            headless=BrowserConfig.headless,

            slow_mo=BrowserConfig.slow_mo

        )

        context = browser.new_context()

        page = context.new_page()

        self.session.browser = browser

        self.session.context = context

        self.session.page = page

        return self.session

    def stop(self):

        self.session.browser.close()

        self.playwright.stop()
    def start(self, profile="default"):

        self.playwright = sync_playwright().start()

        browser = self.playwright.chromium.launch(
        headless=BrowserConfig.headless,
        slow_mo=BrowserConfig.slow_mo
    )

    storage = Path(
        f"outputs/storage/{profile}.json"
    )

    if storage.exists():

        context = browser.new_context(
            storage_state=str(storage)
        )

    else:

        context = browser.new_context()

    page = context.new_page()


