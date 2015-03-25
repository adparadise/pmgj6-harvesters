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
        self.velocity = [0, 0]

        self.sprite.color.r = 0.0
        self.sprite.color.g = 0.2
        self.sprite.color.b = 0.5
        self.sprite.setSizeScalar(30)

        self.canvas.add(self.sprite.canvas)

        self.shouldRemove = False

    def reset(self, isRespawned):
        sample = random.random()
        theta = math.pi * 2 * sample
        speed = 0.1
        self.isRespawned = isRespawned
        self.velocity = [math.cos(theta) * speed,
                         math.sin(theta) * speed]

    def setWorld(self, world):
        self.world = world

    def setCenterPos(self, centerPos):
    	self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

    def update(self, dt):
        centerPos = (self.pos[0] + self.velocity[0] + self.world.direction[0] * self.world.speed,
                     self.pos[1] + self.velocity[1] + self.world.direction[1] * self.world.speed)

        if self.isRespawned:
            print centerPos
            self.isRespawned = False

        if centerPos[0] < self.world.left:
            self.shouldRemove = True

        if centerPos[0] > self.world.right:
            self.shouldRemove = True

        if centerPos[1] < self.world.left:
            self.shouldRemove = True

        if centerPos[1] > self.world.right:
            self.shouldRemove = True

        self.setCenterPos(centerPos)
