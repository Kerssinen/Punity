import pygame
from abc import ABC, abstractmethod

class GameBehaviour:

    def __init__(self):
        super().__init__()
        self.gameobjects = []

    def instantiate(self, object):
        self.gameobjects.append(object)

    def updateAll(self):
        for object in self.gameobjects:
            object.update()
            object.update_components()
