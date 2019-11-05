from component import Component

class EventListener(Component):
    def __init__(self, object, response):
        super().__init__(object)
        self.response = response

    def on_event_raised(self):
        self.response()