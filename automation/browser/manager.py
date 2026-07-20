from automation.browser.browser import BrowserEngine


class BrowserManager:

    def __init__(self):

        self.engine = BrowserEngine()

        self.session = None

    def start(self):

        self.session = self.engine.start()

    def stop(self):

        self.engine.stop()

    def page(self):

        return self.session.page
