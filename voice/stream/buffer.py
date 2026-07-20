from collections import deque

class AudioBuffer:

    def __init__(self, size=50):

        self.buffer = deque(maxlen=size)

    def push(self, frame):

        self.buffer.append(frame)

    def get(self):

        return list(self.buffer)

    def clear(self):

        self.buffer.clear()