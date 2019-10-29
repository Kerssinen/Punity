import pygame

def init_display(width, depth):
    global screen
    screen = pygame.display.set_mode((width, depth))
