import time
import os
from voice.stt import stt_engine
from voice.tts import tts_engine
from integrations.databases.sqlite import db

class VoiceAssistantManager:

    def __init__(self):
        self.is_listening = False
        self.listeners = []

    def add_listener(self, callback):
        """Add GUI / Event listener callback."""
        self.listeners.append(callback)

    def _notify(self, event_type: str, data: dict):
        for callback in self.listeners:
            try:
                callback(event_type, data)
            except Exception as e:
                print(f"Listener notification error: {e}")

    def process_voice_input(self, user_speech: str) -> str:
        """Process user speech through AI and speak back response while storing log in SQLite DB."""
        if not user_speech:
            return ""

        start_time = time.time()
        self._notify("user_speech", {"text": user_speech})

        # Generate JARVIS AI response
        response = self.generate_jarvis_response(user_speech)
        latency = round(time.time() - start_time, 3)

        # Log interaction in SQLite database
        db.log_voice(user_input=user_speech, jarvis_response=response, source="voice_engine", latency=latency)
        db.log_chat(role="user", content=user_speech)
        db.log_chat(role="assistant", content=response)

        # Speak back response cleanly
        self._notify("jarvis_response", {"text": response, "latency": latency})
        tts_engine.speak(response, async_mode=True)

        return response

    def generate_jarvis_response(self, text: str) -> str:
        text_lower = text.lower()
        if "status" in text_lower or "report" in text_lower:
            return "All core systems operational, sir. Security protocols active, database synced."
        elif "open browser" in text_lower or "google" in text_lower:
            return "Opening browser automation suite."
        elif "excel" in text_lower or "office" in text_lower:
            return "Office automation ready. Workbook initialized."
        elif "who are you" in text_lower or "identity" in text_lower:
            return "I am JARVIS, your Autonomous AI Assistant."
        else:
            return f"Understood, sir. Processing: {text}"

    def listen_and_process(self):
        """Capture live voice from microphone and execute pipeline."""
        print("🎙 Listening for voice command...")
        self._notify("status", {"state": "listening"})
        
        speech = stt_engine.listen_live(timeout=5)
        if speech:
            self.process_voice_input(speech)
        else:
            self._notify("status", {"state": "idle"})
            print("No speech detected.")

voice_manager = VoiceAssistantManager()
