import pygame
from component import Component
import display

class SpriteRenderer(Component):
    def __init__(self, object, image):
        super().__init__(object)
        self.sprite = pygame.image.load(image).convert_alpha()

    def draw(self):
        temp_sprite = pygame.transform.rotate(self.sprite, 360 - self.gameobject.transform.rotation)
        temp_sprite = pygame.transform.scale(temp_sprite, (int(self.gameobject.transform.size.x * temp_sprite.get_width()), int(self.gameobject.transform.size.y * temp_sprite.get_height())))
        display.screen.blit(temp_sprite, pygame.math.Vector2(self.gameobject.transform.position.x - temp_sprite.get_width() / 2, self.gameobject.transform.position.y - temp_sprite.get_height() / 2))
        #pygame.draw.rect(display.screen, (0,0,0), (self.gameobject.transform.position.x, self.gameobject.transform.position.y, 100, 100))