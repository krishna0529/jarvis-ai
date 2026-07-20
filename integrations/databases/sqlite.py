import sqlite3
import os
import json
from datetime import datetime

class SQLiteDatabase:

    def __init__(self, db_path="data/jarvis.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Voice logs table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS voice_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    user_input TEXT,
                    jarvis_response TEXT,
                    source TEXT,
                    latency REAL
                )
            """)
            
            # Chat history table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    role TEXT,
                    content TEXT
                )
            """)
            
            # System events log table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS system_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    level TEXT,
                    module TEXT,
                    message TEXT
                )
            """)
            
            # Settings table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated_at TEXT
                )
            """)
            
            conn.commit()

    def log_voice(self, user_input: str, jarvis_response: str, source: str = "mic", latency: float = 0.0):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO voice_logs (timestamp, user_input, jarvis_response, source, latency)
                VALUES (?, ?, ?, ?, ?)
            """, (datetime.utcnow().isoformat(), user_input, jarvis_response, source, latency))
            conn.commit()

    def get_voice_logs(self, limit: int = 50):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM voice_logs ORDER BY id DESC LIMIT ?", (limit,))
            return [dict(row) for row in cursor.fetchall()]

    def log_chat(self, role: str, content: str):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO chat_history (timestamp, role, content)
                VALUES (?, ?, ?)
            """, (datetime.utcnow().isoformat(), role, content))
            conn.commit()

    def get_chat_history(self, limit: int = 50):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM chat_history ORDER BY id ASC LIMIT ?", (limit,))
            return [dict(row) for row in cursor.fetchall()]

    def log_system_event(self, level: str, module: str, message: str):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO system_logs (timestamp, level, module, message)
                VALUES (?, ?, ?, ?)
            """, (datetime.utcnow().isoformat(), level, module, message))
            conn.commit()

    def set_setting(self, key: str, value):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            str_val = json.dumps(value)
            cursor.execute("""
                INSERT OR REPLACE INTO settings (key, value, updated_at)
                VALUES (?, ?, ?)
            """, (key, str_val, datetime.utcnow().isoformat()))
            conn.commit()

    def get_setting(self, key: str, default=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
            row = cursor.fetchone()
            if row:
                try:
                    return json.loads(row["value"])
                except Exception:
                    return row["value"]
            return default

# Singleton instance
db = SQLiteDatabase()
