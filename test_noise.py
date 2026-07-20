from voice.noise.manager import NoiseManager

noise = NoiseManager()

file = noise.clean()

print("Clean Audio:", file)