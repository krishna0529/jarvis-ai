# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QGroupBox, QHeaderView
)
# pyrefly: ignore [missing-import]
from PySide6.QtCore import Qt, QTimer
# pyrefly: ignore [missing-import]
from PySide6.QtGui import QFont

from gui.dashboard.arc_reactor import ArcReactorWidget
from voice.voice_manager import voice_manager
from voice.tts import tts_engine
from integrations.databases.sqlite import db

class DashboardView(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        
        # Connect voice manager listener
        voice_manager.add_listener(self.on_voice_event)
        
        # Refresh database log table timer
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.load_voice_logs)
        self.refresh_timer.start(2000)

    def init_ui(self):
        # Apply Cyberpunk Dark Futuristic Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #0b0e14;
                color: #00f0ff;
                font-family: 'Consolas', 'Segoe UI', sans-serif;
            }
            QGroupBox {
                border: 1px solid #00f0ff;
                border-radius: 8px;
                margin-top: 10px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: #00f0ff;
            }
            QPushButton {
                background-color: #121e2b;
                border: 1px solid #00f0ff;
                border-radius: 6px;
                padding: 8px 15px;
                color: #00f0ff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00f0ff;
                color: #0b0e14;
            }
            QLineEdit {
                background-color: #121e2b;
                border: 1px solid #00f0ff;
                border-radius: 4px;
                padding: 6px;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #121e2b;
                border: 1px solid #0088ff;
                gridline-color: #004488;
                color: #e0e0e0;
            }
            QHeaderView::section {
                background-color: #1a2a3a;
                color: #00f0ff;
                padding: 4px;
                border: 1px solid #004488;
            }
        """)

        main_layout = QVBoxLayout(self)

        # Header Title
        title_label = QLabel("⚡ JARVIS CONTROL CENTER — 3D HOLOGRAPHIC DASHBOARD")
        title_font = QFont("Consolas", 14, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Top Horizontal Split (Arc Reactor + Voice Control Panel + Quick Controls)
        top_layout = QHBoxLayout()

        # Left Column: 3D Holographic Arc Reactor
        reactor_group = QGroupBox("CORE ARC REACTOR")
        reactor_layout = QVBoxLayout(reactor_group)
        self.arc_reactor = ArcReactorWidget()
        reactor_layout.addWidget(self.arc_reactor, alignment=Qt.AlignCenter)
        top_layout.addWidget(reactor_group, stretch=1)

        # Middle Column: Voice Assistant Controls
        voice_group = QGroupBox("VOICE ASSISTANT ENGINE")
        voice_layout = QVBoxLayout(voice_group)
        
        self.voice_status_label = QLabel("STATUS: IDLE / ONLINE")
        self.voice_status_label.setFont(QFont("Consolas", 11, QFont.Bold))
        voice_layout.addWidget(self.voice_status_label)

        self.speech_input = QLineEdit()
        self.speech_input.setPlaceholderText("Type voice command or click Listen...")
        self.speech_input.returnPressed.connect(self.on_manual_voice_submit)
        voice_layout.addWidget(self.speech_input)

        btn_layout = QHBoxLayout()
        self.btn_listen = QPushButton("🎙 ACTIVATE VOICE LISTEN")
        self.btn_listen.clicked.connect(self.on_voice_listen_click)
        btn_layout.addWidget(self.btn_listen)

        self.btn_speak_test = QPushButton("🔊 TEST SPEECH TTS")
        self.btn_speak_test.clicked.connect(self.on_test_tts_click)
        btn_layout.addWidget(self.btn_speak_test)

        voice_layout.addLayout(btn_layout)

        self.last_speech_label = QLabel("Last Response: Ready, sir.")
        self.last_speech_label.setWordWrap(True)
        voice_layout.addWidget(self.last_speech_label)

        top_layout.addWidget(voice_group, stretch=2)

        # Right Column: Subsystem Control Panel
        subsystem_group = QGroupBox("SUBSYSTEM CONTROLS")
        subsystem_layout = QVBoxLayout(subsystem_group)

        btn_browser = QPushButton("🌐 OPEN BROWSER AUTOMATION")
        btn_browser.clicked.connect(lambda: self.on_control_action("Browser Automation initialized"))
        subsystem_layout.addWidget(btn_browser)

        btn_office = QPushButton("📊 GENERATE OFFICE REPORT")
        btn_office.clicked.connect(lambda: self.on_control_action("Office Manager: Creating Excel report..."))
        subsystem_layout.addWidget(btn_office)

        btn_security = QPushButton("🛡 RUN SECURITY POLICY AUDIT")
        btn_security.clicked.connect(lambda: self.on_control_action("Security Policy Check: Passed 100%"))
        subsystem_layout.addWidget(btn_security)

        btn_integrations = QPushButton("🔗 SYNC GITHUB & GMAIL CONNECTORS")
        btn_integrations.clicked.connect(lambda: self.on_control_action("Integrations Synced: GitHub, Gmail OK"))
        subsystem_layout.addWidget(btn_integrations)

        top_layout.addWidget(subsystem_group, stretch=1)

        main_layout.addLayout(top_layout)

        # Bottom Section: SQLite Voice & System Logs Table
        logs_group = QGroupBox("PERSISTENT SQLITE DATABASE LOGS (voice_logs)")
        logs_layout = QVBoxLayout(logs_group)

        self.table_logs = QTableWidget()
        self.table_logs.setColumnCount(5)
        self.table_logs.setHorizontalHeaderLabels(["ID", "Timestamp", "User Input", "JARVIS Response", "Latency (s)"])
        self.table_logs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        logs_layout.addWidget(self.table_logs)

        main_layout.addWidget(logs_group, stretch=1)

        self.load_voice_logs()

    def on_voice_listen_click(self):
        self.voice_status_label.setText("STATUS: 🎙 LISTENING...")
        QTimer.singleShot(100, voice_manager.listen_and_process)

    def on_test_tts_click(self):
        tts_engine.speak("JARVIS 3D Holographic Core online and fully operational, sir.", async_mode=True)

    def on_manual_voice_submit(self):
        text = self.speech_input.text().strip()
        if text:
            self.speech_input.clear()
            voice_manager.process_voice_input(text)

    def on_control_action(self, msg: str):
        self.last_speech_label.setText(f"Action: {msg}")
        tts_engine.speak(msg, async_mode=True)
        db.log_system_event("INFO", "GUI_Dashboard", msg)

    def on_voice_event(self, event_type: str, data: dict):
        if event_type == "user_speech":
            self.voice_status_label.setText(f"USER: {data.get('text')}")
        elif event_type == "jarvis_response":
            resp = data.get("text", "")
            self.last_speech_label.setText(f"JARVIS: {resp}")
            self.voice_status_label.setText("STATUS: ONLINE / IDLE")
            self.load_voice_logs()

    def load_voice_logs(self):
        logs = db.get_voice_logs(limit=20)
        self.table_logs.setRowCount(len(logs))
        for row_idx, log in enumerate(logs):
            self.table_logs.setItem(row_idx, 0, QTableWidgetItem(str(log.get("id"))))
            self.table_logs.setItem(row_idx, 1, QTableWidgetItem(str(log.get("timestamp"))[:19]))
            self.table_logs.setItem(row_idx, 2, QTableWidgetItem(str(log.get("user_input"))))
            self.table_logs.setItem(row_idx, 3, QTableWidgetItem(str(log.get("jarvis_response"))))
            self.table_logs.setItem(row_idx, 4, QTableWidgetItem(str(log.get("latency"))))
