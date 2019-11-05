from game_object import GameObject
from sprite_renderer import SpriteRenderer
import display
import pygame
import utils
from explosion import Explosion
from bullet import Bullet
from rigidbody import Rigidbody
from gun import Gun
from event_listener import EventListener
from game_event import GameEvent
import copy

class Player(GameObject):
    def __init__(self, texture, speed):
        super().__init__()
        self.sr = SpriteRenderer(self, texture)
        self.rb = Rigidbody(self)

        self.event_listener = EventListener(self, self.explode)
        self.event = GameEvent(self)

        self.add_components([self.rb, self.sr, self.event_listener])

        self.gun = Gun()
        self.gun.transform.set_parent(self.transform)
        self.gun.transform.local_position = pygame.math.Vector2(0, -32)
        self.instantiate(self.gun)

        self.speed = speed

        self.transform.size = pygame.math.Vector2(3,3)
        self.cooldown = 0.5
        self.cooldown_timer = 0

        self.vel = pygame.math.Vector2(0,0)
        self.acc = 100
        self.dec = 0.8

    def update(self):
        self.move()

    def move(self):
        if self.input(pygame.K_a):
            self.vel.x = self.vel.x - self.acc
        if self.input(pygame.K_d):
            self.vel.x = self.vel.x + self.acc
        if self.input(pygame.K_w):
            self.vel.y = self.vel.y - self.acc
        if self.input(pygame.K_s):
            self.vel.y = self.vel.y + self.acc
        
        if self.vel.magnitude() > self.speed:
            self.vel = self.vel.normalize() * self.speed

        self.rb.velocity = self.vel

        self.vel *= self.dec
        if self.vel.magnitude() < 0.01:
            self.vel = pygame.math.Vector2(0,0)
            
        if self.input(pygame.K_LEFT):
            self.transform.rotation = 270
            if self.cooldown_timer >= self.cooldown:
                self.shoot(pygame.math.Vector2(-1, 0))
                self.event.raise_event()
                self.cooldown_timer = 0
        if self.input(pygame.K_RIGHT):
            self.transform.rotation = 90
            if self.cooldown_timer >= self.cooldown:
                self.shoot(pygame.math.Vector2(1, 0))
                self.event.raise_event()
                self.cooldown_timer = 0
        if self.input(pygame.K_UP):
            self.transform.rotation = 0
            if self.cooldown_timer >= self.cooldown:
                self.shoot(pygame.math.Vector2(0, -1))
                self.event.raise_event()
                self.cooldown_timer = 0
        if self.input(pygame.K_DOWN):
            self.transform.rotation = 180
            if self.cooldown_timer >= self.cooldown:
                self.shoot(pygame.math.Vector2(0, 1))
                self.event.raise_event()
                self.cooldown_timer = 0

        self.cooldown_timer += utils.dt

        #-- DEBUGGING --#
        pygame.draw.line(display.screen, (255,255,255), self.transform.position, self.transform.position + self.vel)
        #-- DEBUGGING --#

        #if self.input(pygame.K_SPACE) and self.cooldown_timer >= self.cooldown:
    def explode(self):
        explosion = Explosion()
        self.instantiate(explosion, self.transform.position)
        explosion.pe.spawn()
        self.cooldown_timer = 0

    def shoot(self, dir):
        bullet = Bullet(self.transform.forward())
        bullet.transform.scale(2,2)
        bullet.rb.velocity = bullet.rb.velocity + self.rb.velocity
        self.instantiate(bullet, self.gun.transform.position)
