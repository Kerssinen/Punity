import pygame
class Vihu:
    def __init__(self, x, y):
        self.kuva = pygame.image.load("enema.png").convert_alpha()
        self.x=x
        self.y=y
