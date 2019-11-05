import pygame
from abc import ABC, abstractmethod

gameobjects = []
removables = []

def updateAll():

    for r in removables:
        if r in gameobjects:
            gameobjects.remove(r)
    for object in gameobjects:
        object.update()
    for object in gameobjects:
        object.update_components()
    for object in gameobjects:
        object.transform.update()
    for object in gameobjects:
        object.draw_sprites()
    
