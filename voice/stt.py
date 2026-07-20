import os
import time

class SpeechToTextEngine:

    def __init__(self):
        self.sr_available = False
        try:
            import speech_recognition as sr
            self.recognizer = sr.Recognizer()
            self.sr_available = True
        except ImportError:
            self.recognizer = None

    def transcribe_file(self, audio_file_path: str) -> str:
        """Transcribe audio file to text."""
        if not os.path.exists(audio_file_path):
            return ""

        if self.sr_available:
            import speech_recognition as sr
            try:
                with sr.AudioFile(audio_file_path) as source:
                    audio_data = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio_data)
                    return text
            except Exception as e:
                print(f"STT Error: {e}")
                return ""
        else:
            print("SpeechRecognition library not installed. Returning simulation placeholder.")
            return "JARVIS, status report"

    def listen_live(self, timeout=5) -> str:
        """Listen live from default microphone."""
        if self.sr_available:
            import speech_recognition as sr
            try:
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=timeout)
                    return self.recognizer.recognize_google(audio)
            except Exception as e:
                print(f"Live Listen error: {e}")
                return ""
        return ""

stt_engine = SpeechToTextEngine()
