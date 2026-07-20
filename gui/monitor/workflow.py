# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class WorkflowMonitorView(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Workflow Monitor View"))
