# pyrefly: ignore [missing-import]
from faster_whisper import WhisperModel

from voice.stt.config import *

from voice.stt.gpu import DeviceManager

class WhisperEngine:

    def __init__(self):

        self.model = WhisperModel(

            MODEL,

            device=DeviceManager.get(),

            compute_type=COMPUTE_TYPE

        )

    def transcribe(self, audio):

        segments, info = self.model.transcribe(

            audio,

            beam_size=BEAM_SIZE,

            language=LANGUAGE,

            vad_filter=VAD_FILTER

        )

        return segments, info