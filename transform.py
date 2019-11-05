import pygame
import math

class Transform:
    def __init__(self, position = pygame.math.Vector2(0, 0), rotation = 0, size = pygame.math.Vector2(1, 1)):
        self.position = position
        self.rotation = rotation
        self.size = size

        self.local_position = pygame.math.Vector2(0, 0)
        self.local_rotation = 0
        self.local_size = pygame.math.Vector2(1, 1)

        self.parent = None

    def rotate(self, amount):
        self.rotation += amount
        self.rotation = self.rotation

    def scale(self, width, height):
        if width >= 0:
            self.size.x = width
        if height >= 0:
            self.size.y = height

    def forward(self):
        return pygame.math.Vector2(math.sin(math.radians(self.rotation)), -math.cos(math.radians(self.rotation))).normalize()

    def set_parent(self, parent):
        self.parent = parent

    def update(self):
        if self.parent != None:
            self.position = self.parent.position + self.local_position.rotate(self.parent.rotation)
            self.rotation = self.parent.rotation + self.local_rotation
            self.size.x = self.parent.size.x * self.local_size.x
            self.size.y = self.parent.size.y * self.local_size.y
