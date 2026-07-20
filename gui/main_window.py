# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS Control Center")
        self.resize(1024, 768)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        label = QLabel("JARVIS Application Shell")
        layout.addWidget(label)
        
        self.setCentralWidget(central_widget)
