class EventBus:

    def __init__(self):

        self.subscribers = {}

    def subscribe(self, event_name, handler):

        self.subscribers.setdefault(event_name, []).append(handler)

    def publish(self, event):

        for handler in self.subscribers.get(event.name, []):

            handler(event)
