import os
import threading

class TextToSpeechEngine:

    def __init__(self):
        self.engine_type = None
        self.pyttsx3_engine = None
        
        # Try pyttsx3
        try:
            # pyrefly: ignore [missing-import]
            import pyttsx3
            self.pyttsx3_engine = pyttsx3.init()
            self.pyttsx3_engine.setProperty('rate', 175)
            self.pyttsx3_engine.setProperty('volume', 1.0)
            voices = self.pyttsx3_engine.getProperty('voices')
            # Select male/AI voice if available
            for voice in voices:
                if "david" in voice.name.lower() or "jarvis" in voice.name.lower():
                    self.pyttsx3_engine.setProperty('voice', voice.id)
                    break
            self.engine_type = "pyttsx3"
        except Exception:
            # Fallback to SAPI5 on Windows
            try:
                import win32com.client
                self.sapi_voice = win32com.client.Dispatch("SAPI.SpVoice")
                self.engine_type = "sapi5"
            except Exception:
                self.engine_type = "print_only"

    def speak(self, text: str, async_mode: bool = True):
        """Speak out text cleanly."""
        print(f"[JARVIS Voice Output]: {text}")

        if async_mode:
            threading.Thread(target=self._speak_internal, args=(text,), daemon=True).start()
        else:
            self._speak_internal(text)

    def _speak_internal(self, text: str):
        if self.engine_type == "pyttsx3" and self.pyttsx3_engine:
            try:
                self.pyttsx3_engine.say(text)
                self.pyttsx3_engine.runAndWait()
            except Exception as e:
                print(f"TTS Speech error: {e}")
        elif self.engine_type == "sapi5":
            try:
                self.sapi_voice.Speak(text)
            except Exception as e:
                print(f"SAPI5 Speech error: {e}")

tts_engine = TextToSpeechEngine()
