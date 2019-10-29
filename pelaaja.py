import pygame
class Pelaaja:
    def __init__(self, x, y):
        self.kuva = pygame.image.load("heart.png").convert_alpha()
        self.x=x
        self.y=y
