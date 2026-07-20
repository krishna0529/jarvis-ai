# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QStatusBar
)
# pyrefly: ignore [missing-import]
from PySide6.QtCore import Qt
# pyrefly: ignore [missing-import]
from PySide6.QtGui import QFont

from gui.dashboard.dashboard import DashboardView
from gui.chat.chat import ChatView
from gui.voice.panel import VoiceControlPanel
from gui.monitor.workflow import WorkflowMonitorView
from gui.settings.general import GeneralSettingsView

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS Enterprise AI — 3D Cyberpunk Control Center")
        self.resize(1280, 800)
        self.init_ui()

    def init_ui(self):
        # Global dark cyberpunk stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0b0e14;
            }
            QStatusBar {
                background-color: #121e2b;
                color: #00f0ff;
                border-top: 1px solid #00f0ff;
            }
        """)

        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Sidebar Navigation
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #080b10;
                border-right: 1px solid #00f0ff;
            }
            QPushButton {
                background-color: transparent;
                color: #00f0ff;
                border: none;
                border-left: 3px solid transparent;
                padding: 12px 15px;
                text-align: left;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #121e2b;
                border-left: 3px solid #00f0ff;
            }
            QPushButton:checked {
                background-color: #1a2a3a;
                border-left: 3px solid #00f0ff;
                color: #ffffff;
            }
        """)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 10, 0, 10)

        brand_label = QLabel(" 🤖 JARVIS AI v0.2")
        brand_label.setFont(QFont("Consolas", 14, QFont.Bold))
        brand_label.setStyleSheet("color: #00f0ff; padding: 15px 10px;")
        sidebar_layout.addWidget(brand_label)

        # Navigation Buttons
        self.btn_dashboard = QPushButton(" 📊 3D Dashboard")
        self.btn_chat = QPushButton(" 💬 AI Chat")
        self.btn_voice = QPushButton(" 🎙 Voice Control")
        self.btn_monitor = QPushButton(" 📈 System Monitor")
        self.btn_settings = QPushButton(" ⚙ Settings")

        for btn in [self.btn_dashboard, self.btn_chat, self.btn_voice, self.btn_monitor, self.btn_settings]:
            btn.setCheckable(True)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()

        status_label = QLabel(" Status: Core Active")
        status_label.setStyleSheet("color: #00ffaa; font-size: 11px; padding: 10px;")
        sidebar_layout.addWidget(status_label)

        main_layout.addWidget(sidebar)

        # Stacked Views Container
        self.stack = QStackedWidget()
        
        self.dashboard_view = DashboardView()
        self.chat_view = ChatView()
        self.voice_view = VoiceControlPanel()
        self.monitor_view = WorkflowMonitorView()
        self.settings_view = GeneralSettingsView()

        self.stack.addWidget(self.dashboard_view)
        self.stack.addWidget(self.chat_view)
        self.stack.addWidget(self.voice_view)
        self.stack.addWidget(self.monitor_view)
        self.stack.addWidget(self.settings_view)

        main_layout.addWidget(self.stack)

        self.setCentralWidget(central_widget)

        # Connect Navigation
        self.btn_dashboard.clicked.connect(lambda: self.switch_view(0, self.btn_dashboard))
        self.btn_chat.clicked.connect(lambda: self.switch_view(1, self.btn_chat))
        self.btn_voice.clicked.connect(lambda: self.switch_view(2, self.btn_voice))
        self.btn_monitor.clicked.connect(lambda: self.switch_view(3, self.btn_monitor))
        self.btn_settings.clicked.connect(lambda: self.switch_view(4, self.btn_settings))

        # Default selection
        self.btn_dashboard.setChecked(True)

        # Status bar
        status_bar = QStatusBar()
        status_bar.showMessage("JARVIS Autonomous AI Engine Connected | Database: Active | 3D Arc-Reactor Online")
        self.setStatusBar(status_bar)

    def switch_view(self, index: int, active_btn):
        for btn in [self.btn_dashboard, self.btn_chat, self.btn_voice, self.btn_monitor, self.btn_settings]:
            btn.setChecked(False)
        active_btn.setChecked(True)
        self.stack.setCurrentIndex(index)
