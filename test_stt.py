from voice.stt.manager import SpeechManager

speech = SpeechManager()

segments, info = speech.listen(

    "data/clean.wav"

)

print(info.language)

for segment in segments:

    print(segment.text)