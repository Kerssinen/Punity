from game_object import GameObject
from sprite_renderer import SpriteRenderer
import display
import pygame
import utils

class Player(GameObject):
    def __init__(self, texture, speed):
        super().__init__()
        self.sr = SpriteRenderer(self, texture)
        self.add_component(self.sr)
        self.scale = 1
        self.speed = speed

    def update(self):

        keys = pygame.key.get_pressed()
        dir = rot = scale = pygame.math.Vector2(0,0)

        if keys[pygame.K_LEFT]:
            dir.x = -1
        if keys[pygame.K_RIGHT]:
            dir.x = 1
        if keys[pygame.K_UP]:
            dir.y = -1
        if keys[pygame.K_DOWN]:
            dir.y = 1

        if dir.magnitude() > 0:
            self.transform.position += dir.normalize() * self.speed * utils.dt

        if keys[pygame.K_a]:
            self.transform.rotate(10)
        if keys[pygame.K_d]:
            self.transform.rotate(-10)

        if keys[pygame.K_w]:
            self.scale += 1
            self.transform.scale(self.scale,self.scale)
        if keys[pygame.K_s]:
            self.scale -= 1
            self.transform.scale(self.scale,self.scale)
