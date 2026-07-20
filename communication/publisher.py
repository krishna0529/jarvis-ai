from communication.event import Event

class EventPublisher:

    def __init__(self, event_bus):

        self.event_bus = event_bus

    def publish(self, name: str, payload: dict, source: str = ""):

        event = Event(name=name, payload=payload, source=source)

        self.event_bus.publish(event)
