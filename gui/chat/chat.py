# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ChatView(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("AI Chat Interface"))
