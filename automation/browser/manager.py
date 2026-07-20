from automation.browser.smart_locator import SmartLocator
from automation.browser.browser import BrowserEngine
from automation.browser.page import PageManager
from automation.browser.locator import LocatorManager
from automation.browser.actions import ActionManager
from automation.browser.screenshot import ScreenshotManager
from automation.browser.pdf import PDFManager
from automation.browser.download import DownloadManager
from automation.browser.upload import UploadManager
from automation.browser.cookies import CookieManager
from automation.browser.storage import StorageStateManager
from automation.browser.wait import WaitManager





class BrowserManager:

    def __init__(self):

        self.engine = BrowserEngine()

        self.session = None

        self.page = None

        self.locator = None

    def start(self, profile="default"):

        self.session = self.engine.start(profile)
        # self.session = self.engine.start()
        self.page = PageManager(self.session.page)

        self.locator = LocatorManager(self.session.page)

        self.actions = ActionManager(self.session.page)

        self.screenshot = ScreenshotManager(
            self.session.page
        )
        self.smart = SmartLocator(
            self.session.page
        )
        self.pdf = PDFManager(
            self.session.page
        )
        self.wait = WaitManager(
            self.session.page
        )

        self.download = DownloadManager(
            self.session.page
        )

        self.upload = UploadManager(
            self.session.page
        )
        self.page = PageManager(
            self.session.page
        )

        self.locator = LocatorManager(
            self.session.page
        )

        self.actions = ActionManager(
            self.session.page
        )

        self.storage = StorageStateManager(
            self.session.context
        )

        self.cookies = CookieManager(
            self.session.context
        )

    def stop(self):

        self.engine.stop()