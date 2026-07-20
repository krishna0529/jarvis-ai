from voice.noise.reducer import NoiseReducer
from voice.noise.factory import NoiseFactory


class NoiseManager:

    def __init__(self):

        self.reducer = NoiseReducer()

    def clean(self):

        return self.reducer.reduce(
            "data/input.wav",
            "data/clean.wav"
        )
class NoiseManager:

    def __init__(self):
        self.engine = NoiseFactory.create()

    def clean(self, audio):
        return self.engine.reduce(audio)