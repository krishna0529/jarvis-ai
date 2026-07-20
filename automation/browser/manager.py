from automation.browser.browser import BrowserEngine
from automation.browser.page import PageManager
from automation.browser.locator import LocatorManager
from automation.browser.actions import ActionManager
from automation.browser.screenshot import ScreenshotManager
from automation.browser.pdf import PDFManager
from automation.browser.download import DownloadManager
from automation.browser.upload import UploadManager


class BrowserManager:

    def start(self):

        self.session = self.engine.start()

        self.page = PageManager(self.session.page)

        self.locator = LocatorManager(self.session.page)

        self.actions = ActionManager(self.session.page)

        self.screenshot = ScreenshotManager(
            self.session.page
        )

        self.pdf = PDFManager(
            self.session.page
        )

        self.download = DownloadManager(
            self.session.page
        )

        self.upload = UploadManager(
            self.session.page
        )


class BrowserManager:

    def __init__(self):

        self.engine = BrowserEngine()

        self.session = None

        self.page = None

        self.locator = None

    def start(self):

        self.session = self.engine.start()

        self.page = PageManager(
            self.session.page
        )

        self.locator = LocatorManager(
            self.session.page
        )

    def stop(self):

        self.engine.stop()