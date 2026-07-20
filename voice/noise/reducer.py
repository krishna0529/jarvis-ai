# pyrefly: ignore [missing-import]
import noisereduce as nr
# pyrefly: ignore [missing-import]
import soundfile as sf

from voice.noise.config import *


class NoiseReducer:

    def reduce(self, input_file, output_file):

        audio, sr = sf.read(input_file)

        clean_audio = nr.reduce_noise(
            y=audio,
            sr=sr,
            stationary=STATIONARY,
            prop_decrease=PROP_DECREASE
        )

        sf.write(output_file, clean_audio, sr)

        return output_file