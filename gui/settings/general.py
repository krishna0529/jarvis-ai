# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class GeneralSettingsView(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("General Settings"))
