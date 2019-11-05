import pygame
from game_object import GameObject
from game_event import GameEvent

class Item(GameObject):
    def __init__(self):
        super().__init__()
        self.event = GameEvent(self)

    def update(self):
        if self.input(pygame.K_SPACE):
            self.event.raise_event()