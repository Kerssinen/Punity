import pygame
import utils
from enum import Enum, auto
from component import Component
import display
import random

class ParticleEffect(Component):
    def __init__(self, object, image = None, scale = pygame.math.Vector2(40,40), color = pygame.Color(0,0,0)):
        super().__init__(object)

        # PARTICLE PROPERTIES
        self.sprite = pygame.image.load(image).convert_alpha()
        self.scale = scale
        self.color = color
        self.gravity = False
        self.speed = 80
        self.lifetime = 1

        # PARTICLESYSTEM PROPERTIES
        self.number_of_particles = 10
        self.loop = True
        self.shape = self.Shape.SPHERE
        self.shape_size = 180
        self.frequency = 1
        self.fade = 7

        self.particles = []

    def spawn(self):
        for i in range(self.number_of_particles):
            particle = self.Particle(self.gameobject.transform.position, pygame.math.Vector2(0,1).rotate(self.gameobject.transform.rotation - self.shape_size / 2 + i * self.shape_size / self.number_of_particles), self.speed, self.fade)
            self.particles.append(particle)

    def update(self):
        for p in self.particles:
            # TODO: Use temp_sprites here to apply randomization to rotation and scale
            temp_sprite = self.sprite.copy()
            temp_sprite.fill((255,255,255,p.alpha), None, pygame.BLEND_RGBA_MULT)
            temp_sprite = pygame.transform.scale(temp_sprite, (int(self.scale.x), int(self.scale.y)))
            display.screen.blit(temp_sprite, p.pos)
            p.update()
            if p.time_alive > self.lifetime:
                self.particles.remove(p)

    class Particle:
        def __init__(self, pos, dir, speed, fade):
            self.pos = pos
            self.dir = dir
            self.speed = speed
            self.fade = fade
            self.alpha = 255
            self.time_alive = 0

        def update(self):
            # TODO: Apply randomization to direction here
            self.pos = self.pos + self.dir * self.speed * utils.dt
            if (self.alpha - self.fade) > 0:
                self.alpha = int(self.alpha - self.fade)
            self.time_alive += utils.dt

    class Shape(Enum):
        CONE = auto()
        SPHERE = auto()
