class EventDispatcher:

    def __init__(self, event_bus):

        self.event_bus = event_bus

    def dispatch(self, event):

        self.event_bus.publish(event)
