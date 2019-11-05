from game_object import GameObject
from sprite_renderer import SpriteRenderer

class Gun(GameObject):
    def __init__(self):
        super().__init__()
        self.sr = SpriteRenderer(self, 'gun.png')
        self.add_component(self.sr)
