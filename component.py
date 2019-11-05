from mono_behaviour import MonoBehaviour

class Component(MonoBehaviour):
    def __init__(self, gameobject):
        self.gameobject = gameobject

    def update(self):
        pass

    def draw(self):
        pass
