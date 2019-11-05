import pygame
from game_object import GameObject

class SceneManager(GameObject):
    def __init__(self):
        super().__init__()
        #-- TODO --# Tee custom typestä enum
        self.event = pygame.event.Event(pygame.USEREVENT, custom_type=1)

    def update(self):
        if self.input(pygame.K_ESCAPE):
            pygame.quit()
        if self.input(pygame.K_f):
            pygame.event.post(self.event)