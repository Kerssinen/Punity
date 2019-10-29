import pygame
from component import Component
import display

class SpriteRenderer(Component):
    def __init__(self, object, image):
        super().__init__(object)
        self.sprite = pygame.image.load(image).convert_alpha()

    def update(self):
        temp_sprite = pygame.transform.rotate(self.sprite, self.gameobject.transform.rotation)
        temp_sprite = pygame.transform.scale(temp_sprite, (self.gameobject.transform.width * temp_sprite.get_width(), self.gameobject.transform.height * temp_sprite.get_height()))
        display.screen.blit(temp_sprite, self.gameobject.transform.position)
