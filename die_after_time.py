from component import Component
import utils

class DieAfterTime(Component):
    def __init__(self, object, time):
        super().__init__(object)
        self.time = time
        self.timer = 0

    def update(self):
        self.timer += utils.dt
        if self.timer > self.time:
            self.destroy(self.gameobject)
