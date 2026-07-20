import uuid

class SpeechSession:

    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.partial_text = ""
        self.final_text = ""