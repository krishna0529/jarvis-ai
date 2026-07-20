class ChunkManager:

    def __init__(self):
        self.frames = []

    def add(self, frame):
        self.frames.append(frame)

    def get_chunk(self):
        chunk = self.frames.copy()
        self.frames.clear()
        return chunk