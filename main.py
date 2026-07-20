import sys
# pyrefly: ignore [missing-import]
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from voice.tts import tts_engine
from integrations.databases.sqlite import db

def main():
    print("==================================================")
    print("[JARVIS] STARTING JARVIS ENTERPRISE AI SYSTEM v0.2")
    print("==================================================")
    
    # Log startup event to SQLite database
    db.log_system_event("INFO", "SystemStartup", "JARVIS AI Engine initialized successfully.")
    
    # Announce startup via Text-to-Speech
    tts_engine.speak("JARVIS system online. All core engines operational, sir.", async_mode=True)
    
    # Launch GUI Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
