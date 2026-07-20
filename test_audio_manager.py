from voice.audio_manager import AudioManager

audio = AudioManager()

print(audio.devices())

audio.record()

audio.play()