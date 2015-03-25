from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *

from sprite import Sprite

class Player():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.canvas.add(self.sprite.canvas)

    def setCenterPos(self, centerPos):
        self.sprite.setCenterPos(centerPos)

    def update(self, dt):
        pass
