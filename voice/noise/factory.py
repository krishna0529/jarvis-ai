from voice.noise.reducer import NoiseReducer

class NoiseFactory:

    @staticmethod
    def create():

        return NoiseReducer()
