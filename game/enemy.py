from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *
import math
import random

from sprite import Sprite

class Enemy():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.pos = (0, 0)

        self.sprite.color.r = 0.0
        self.sprite.color.g = 0.2
        self.sprite.color.b = 0.5
        self.sprite.setSizeScalar(30)

        self.canvas.add(self.sprite.canvas)

    def reset(self):
        pass

    def setWorld(self):
        self.world = world

    def setCenterPos(self, centerPos):
    	self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

    def randomPosition(self):
        centerPos = (random.randrange(50, 300), random.randrange(50, 300))
        self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

        theta = math.pi * 0.6
        self.velocity = [math.cos(theta), math.sin(theta)]

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
