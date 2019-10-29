import pygame
from game_object import GameObject
from particle_effect import ParticleEffect

class Explosion(GameObject):
    def __init__(self):
        super().__init__()
        self.pe = ParticleEffect(self, 'heart.png')
        self.add_component(self.pe)
