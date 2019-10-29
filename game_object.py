import pygame
from transform import Transform
import display

class GameObject:
    def __init__(self):
        self.transform = Transform()
        self.components = []

    def update(self):
        pass

    def update_components(self):
        for component in self.components:
            component.update()

    def add_component(self, object):
        self.components.append(object)

    def get_component(self, type):
        for component in self.components:
            if isinstance(component, type):
                return component
        raise Exception('Class', self.__class__.__name__, 'has no component', type.__name__)
