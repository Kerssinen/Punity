from component import Component

class GameEvent(Component):
    def __init__(self, object):
        super().__init__(object)
        self.listeners = []

    def raise_event(self):
        for listener in self.listeners:
            listener.on_event_raised()

    def register_listener(self, listener):
        self.listeners.append(listener)

    def unregister_listener(self, listener):
        self.listeners.remove(listener)