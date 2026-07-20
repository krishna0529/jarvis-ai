from voice.wake_manager import WakeManager

wake = WakeManager()

while True:

    text = input("You : ")

    if wake.listen(text):

        print("JARVIS Activated")

    else:

        print("Sleeping...")