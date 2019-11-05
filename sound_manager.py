from game_object import GameObject
import pygame
from pygame import mixer
from event_listener import EventListener

class SoundManager(GameObject):
    def __init__(self):
        super().__init__()

        mixer.init()
        self.sound_gun = mixer.Sound("s_shot.wav")
        self.event_listener = EventListener(self, self.play_shot_sound)

    def play_shot_sound(self):
        pass
        self.sound_gun.play()