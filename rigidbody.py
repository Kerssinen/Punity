import pygame
import utils
from component import Component

class Rigidbody(Component):
    def __init__(self, object):
        super().__init__(object)
        self.velocity = pygame.math.Vector2(0,0)
        self.angular_velocity = 0
        self.drag = 0
        self.angular_drag = 0

    def update(self):
        self.gameobject.transform.position = self.gameobject.transform.position + self.velocity * utils.dt
        self.gameobject.transform.rotation = self.gameobject.transform.rotation + self.angular_velocity * utils.dt
