import pygame
import utils
from enum import Enum, auto
from component import Component
import display
import random

#-- TODO --#
# Set sprite pivot center
#-- TODO --#

class ParticleEffect(Component):
    def __init__(self, object, image = None, scale = 40, color = pygame.Color(0,0,0)):
        super().__init__(object)

        # PARTICLE PROPERTIES
        self.sprite = pygame.image.load(image).convert_alpha()
        self.start_scale = scale
        self.start_scale_rnd = [-1, 1]
        self.scale_change_rnd = [-50, 50]
        self.color = color
        self.gravity = False
        self.start_speed = 80
        self.speed_rnd = [-40, 40]
        self.start_rotation = 0
        self.start_rotation_rnd = [0, 360]
        self.rotation_change = 0
        self.rotation_change_rnd = [-5, 5]
        self.lifetime = 1

        # PARTICLESYSTEM PROPERTIES
        self.number_of_particles = 10
        self.loop = True
        self.shape = self.Shape.SPHERE
        self.shape_size = 360
        self.frequency = 1
        self.fade = 7

        self.particles = []

    def spawn(self):
        for i in range(self.number_of_particles):
            particle = self.Particle(self.gameobject.transform.position, pygame.math.Vector2(0,1).rotate(self.gameobject.transform.rotation - self.shape_size / 2 + i * self.shape_size / self.number_of_particles), self.start_speed, self.speed_rnd, self.start_rotation, self.start_rotation_rnd, self.rotation_change, self.rotation_change_rnd, self.start_scale, self.start_scale_rnd, self.scale_change_rnd, self.fade)
            self.particles.append(particle)

    def update(self):
        for p in self.particles:
            temp_sprite = self.sprite.copy()
            temp_sprite.fill((255,255,255,p.alpha), None, pygame.BLEND_RGBA_MULT)
            temp_sprite = pygame.transform.rotate(temp_sprite, p.rotation)
            temp_sprite = pygame.transform.scale(temp_sprite, (int(p.scale), int(p.scale)))

            display.screen.blit(temp_sprite, p.pos)
            p.update()
            if p.time_alive > self.lifetime:
                self.particles.remove(p)

    class Particle:
        def __init__(self, pos, dir, speed, speed_rnd, rotation, rotation_rnd, rotation_speed, rotation_speed_rnd, scale, scale_rnd, scale_change_rnd, fade):
            self.pos = pos
            self.dir = dir
            self.speed = speed + speed * random.randrange(speed_rnd[0], speed_rnd[1]) * 0.01
            self.rotation = rotation + random.randrange(rotation_rnd[0], rotation_rnd[1])
            self.rotation_speed = rotation_speed + random.randrange(rotation_speed_rnd[0], rotation_speed_rnd[1])
            self.scale = scale + random.randrange(scale_rnd[0], scale_rnd[1]) * 0.01 * scale
            self.scale_change = random.randrange(scale_change_rnd[0], scale_change_rnd[1]) * 0.01
            self.fade = fade
            self.alpha = 255
            self.time_alive = 0

        def update(self):
            # TODO: Apply randomization to direction here
            self.pos = self.pos + self.dir * self.speed * utils.dt
            self.rotation = self.rotation + self.rotation_speed
            if self.scale + self.scale_change > 0:
                self.scale = self.scale + self.scale_change
            if self.alpha - self.fade > 0:
                self.alpha = int(self.alpha - self.fade)
            self.time_alive += utils.dt

    class Shape(Enum):
        CONE = auto()
        SPHERE = auto()
