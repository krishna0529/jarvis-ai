from voice.noise.live_filter import LiveNoiseFilter

class StreamProcessor:

    def __init__(self):

        self.filter = LiveNoiseFilter()

    def process(self, frame):

        clean = self.filter.process(frame)

        return clean