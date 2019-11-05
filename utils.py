import pygame
pygame.font.init()

clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

font = pygame.font.SysFont("timesnewroman", 72)
text = font.render("Quick Brown Fox Jumped Over The Lazy Dog", True, (0, 128, 0))
