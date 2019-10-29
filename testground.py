import pygame
import utils
from pygame import gfxdraw
import random
from game_object import GameObject
from vihu import Vihu
from pelaaja import Pelaaja
from explosion import Explosion
from luoti import Luoti
import particle_effect

import display
from player import Player
from gameBehaviour import GameBehaviour

display.init_display(1080, 720)

def main():

    pl = Player('heart.png', 500)
    explosion = Explosion()
    explosion.transform.position = pygame.math.Vector2(400,400)
    explosion.pe.spawn()

    gb = GameBehaviour()
    gb.instantiate(pl)
    gb.instantiate(explosion)

    while(True):
        display.screen.fill((0,50,0))

        gb.updateAll()

        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        pygame.display.flip()
        utils.clock.tick(60)

main()
pygame.quit()
