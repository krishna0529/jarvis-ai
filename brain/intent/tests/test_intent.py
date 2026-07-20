from brain.intent.manager import IntentManager

intent = IntentManager()

tests = [
    "Open Chrome",
    "Launch VS Code",
    "Close Excel",
    "Run Notepad",
    "Start Google Chrome"
]

for t in tests:

    result = intent.process(t)

    print(result.model_dump())