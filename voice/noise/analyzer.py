# pyrefly: ignore [missing-import]
import numpy as np

from voice.noise.profile import NoiseProfile

class NoiseAnalyzer:

    def analyze(self, audio):

        rms = np.sqrt(np.mean(audio**2))

        if rms < 0.01:

            return NoiseProfile(
                "silent",
                rms,
                0.20,
                "base"
            )

        elif rms < 0.05:

            return NoiseProfile(
                "office",
                rms,
                0.50,
                "small"
            )

        else:

            return NoiseProfile(
                "noisy",
                rms,
                0.90,
                "medium"
            )