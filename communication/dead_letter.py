class DeadLetterQueue:

    def __init__(self):

        self.failed_events = []

    def add(self, event, error: str):

        self.failed_events.append({
            "event": event,
            "error": error
        })
