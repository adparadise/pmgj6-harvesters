from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *

MIDDLE_X = 330
MIDDLE_Y = 220
ASPECT = 0.95

class Sprite():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.sizeScalar = 50
        self.color = Color(0.0, 0.5, 0.2)
        self.centerPos = (MIDDLE_X, MIDDLE_Y)

        self.rect = Rectangle(pos=(330, 220), size=(50, 45))
        self.setCenterPos((330, 220))
        self.repos()

        self.canvas.add(self.color)
        self.canvas.add(self.rect)

    def repos(self):
        size = (self.sizeScalar, self.sizeScalar * ASPECT)
        self.rect.pos = self.centerPos
        self.rect.size = size

    def setCenterPos(self, centerPos):
        self.centerPos = centerPos
        self.repos()
