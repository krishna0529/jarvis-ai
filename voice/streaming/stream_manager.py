from voice.streaming.audio_queue import AudioQueue
from voice.streaming.chunk_manager import ChunkManager

class StreamingManager:

    def __init__(self):

        self.queue = AudioQueue()

        self.chunk = ChunkManager()

    def receive_audio(self, frame):

        self.queue.push(frame)

    def process(self):

        while not self.queue.empty():

            frame = self.queue.pop()

            self.chunk.add(frame)

        return self.chunk.get_chunk()