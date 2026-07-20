# pyrefly: ignore [missing-import]
import sounddevice as sd
# pyrefly: ignore [missing-import]
import soundfile as sf

class Speaker:

    def play(self, filename):

        data, samplerate = sf.read(filename)

        sd.play(data, samplerate)

        sd.wait()
        