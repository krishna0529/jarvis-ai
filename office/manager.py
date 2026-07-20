from office.excel.manager import ExcelManager
from office.word.manager import WordManager
from office.powerpoint.manager import PowerPointManager
from office.pdf.manager import PDFManager
from office.email.manager import EmailManager

class OfficeManager:

    def __init__(self):
        self.excel = ExcelManager()
        self.word = WordManager()
        self.ppt = PowerPointManager()
        self.pdf = PDFManager()
        self.email = EmailManager()
