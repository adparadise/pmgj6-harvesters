from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *
import random

from sprite import Sprite

class Enemy():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.pos = (0, 0)

        self.sprite.color.r = random.random()
        self.sprite.color.g = random.random()
        self.sprite.color.b = random.random()

        self.canvas.add(self.sprite.canvas)

    def setCenterPos(self, centerPos):
    	self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

    def randomPosition(self):
        centerPos = (random.randrange(50, 300), random.randrange(50, 300))
        self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

        self.velocity = [random.randrange(1, 3), random.randrange(1, 3)]

        if random.randrange(1, 5) < 3:
            self.velocity[0] = -(self.velocity[0])

        if random.randrange(1, 5) < 3:
            self.velocity[1] = -(self.velocity[1])


    def update(self, dt):

        newCoord = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

        if newCoord[0] < 0:
            self.velocity[0] = -(self.velocity[0])

        if newCoord[0] > 700:
            self.velocity[0] = -(self.velocity[0])

        if newCoord[1] < 10:
            self.velocity[1] = -(self.velocity[1])

        if newCoord[1] > 450:
            self.velocity[1] = -(self.velocity[1])

        self.setCenterPos(newCoord)
