import pygame
from game_object import GameObject
from sprite_renderer import SpriteRenderer
from rigidbody import Rigidbody
from die_after_time import DieAfterTime

class Bullet(GameObject):
    def __init__(self, dir):
        super().__init__()
        self.sr = SpriteRenderer(self, 'bullet.png')
        self.rb = Rigidbody(self)
        self.death = DieAfterTime(self, 1)
        self.speed = 500
        self.rb.velocity = dir * self.speed

        self.add_components([self.sr, self.rb, self.death])
