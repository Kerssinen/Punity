import pygame
import gameBehaviour as gb

class MonoBehaviour:
    def __init__(self):
        pass

    def instantiate(self, object, position = pygame.math.Vector2(0, 0), rotation = 0):
        object.transform.position = position
        object.transform.rotation = rotation
        gb.gameobjects.append(object)

    def destroy(self, object):
        gb.removables.append(object)

    def input(self, key):
        keys = pygame.key.get_pressed()
        if keys[key]:
            return True
        return False
