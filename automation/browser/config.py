from dataclasses import dataclass


@dataclass
class BrowserConfig:

    headless = False

    slow_mo = 50

    timeout = 30000
