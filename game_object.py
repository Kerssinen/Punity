import pygame
from transform import Transform
import display
from mono_behaviour import MonoBehaviour

class GameObject(MonoBehaviour):
    def __init__(self):
        self.transform = Transform()
        self.components = []

    def update(self):
        pass

    def update_components(self):
        for component in self.components:
            component.update()

    def draw_sprites(self):
        for component in self.components:
            component.draw()

    def add_component(self, object):
        self.components.append(object)

    def add_components(self, objects):
        for object in objects:
            self.components.append(object)

    def get_component(self, type):
        for component in self.components:
            if isinstance(component, type):
                return component
        raise Exception('Class', self.__class__.__name__, 'has no component', type.__name__)
