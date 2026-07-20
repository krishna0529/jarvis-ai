from voice.stream.buffer import AudioBuffer
from voice.stream.processor import StreamProcessor

class StreamManager:

    def __init__(self):

        self.buffer = AudioBuffer()

        self.processor = StreamProcessor()

    def on_audio(self, frame):

        clean = self.processor.process(frame)

        self.buffer.push(clean)

        return clean