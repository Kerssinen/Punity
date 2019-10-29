import pygame

class Transform:
    def __init__(self, position = pygame.math.Vector2(0,0), rotation = 0, width = 1, height = 1):
        self.position = position
        self.rotation = rotation
        self.width = width
        self.height = height

    def rotate(self, amount):
        self.rotation += amount

    def scale(self, width, height):
        if width >= 0:
            self.width = width
        if height >= 0:
            self.height = height
