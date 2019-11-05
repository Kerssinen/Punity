import pygame
import utils
from pygame import gfxdraw
import random
from game_object import GameObject
from explosion import Explosion
import particle_effect
#import text_field
from scene_manager import SceneManager
from sound_manager import SoundManager

import display
from player import Player
from item import Item
import gameBehaviour as gb

pygame.mixer.pre_init()
pygame.mixer.init()


pygame.init()
display.init_display(1080, 720)

#-- TODO --#
# Colliderit
# Korjaa ääni
# Korjaa ampuminen kääntymisen jälkeen
#-- TODO --#

def main():

    sm = SceneManager()
    sm.instantiate(sm)

    snd_mngr = SoundManager()
    snd_mngr.instantiate(snd_mngr)

    pl = Player('player.png', 400)
    pl.event.register_listener(snd_mngr.event_listener)
    pl.instantiate(pl, pygame.math.Vector2(0,0), 0)
    
    item = Item()
    item.event.register_listener(pl.event_listener)
    item.instantiate(item)

    while(True):
        display.screen.fill((0,50,0))
        gb.updateAll()

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        #text = text_field.create_text("Hello, World", ["comicsansms"], 72, (0, 128, 0))

        #display.screen.blit(text,
        #(320 - text.get_width() // 2, 240 - text.get_height() // 2))

        pygame.display.flip()
        utils.clock.tick(60)
main()
pygame.quit()
