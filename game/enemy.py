from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *
import math
import random

from sprite import Sprite

class Enemy():
    def __init__(self, enemyType, **kwargs):
        self.canvas = InstructionGroup()

        self.enemyType = enemyType
        self.sprite = Sprite()

        if self.enemyType == 'normal':
            self.setOffsetTheta(0)
            self.sprite.color.r = 0.0
            self.sprite.color.g = 0.2
            self.sprite.color.b = 0.5
        else:
            self.setOffsetTheta(math.pi / 2)
            self.sprite.color.r = 0.5
            self.sprite.color.g = 0.1
            self.sprite.color.b = 0.1

        self.health = 100

        self.pos = (0, 0)
        self.velocity = [0, 0]

        self.updateAppearance()

        self.canvas.add(self.sprite.canvas)

        self.shouldRemove = False

    def setOffsetTheta(self, offsetTheta):
        self.offsetTheta = offsetTheta
        self.otcos = math.cos(self.offsetTheta)
        self.otsin = math.sin(self.offsetTheta)


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

    def decrement(self, beamState):
        delta = 0
        if beamState == 1:
            self.health -= 10
            if self.enemyType == 'normal':
                delta = 100
            else:
                delta = -500

        if self.health <= 0:
            self.shouldRemove = True
        else:
            self.updateAppearance()

        return delta



    def updateAppearance(self):
        baseSize = 30
        if not self.enemyType == 'normal':
            baseSize = 15

        factor = math.log(100 - self.health + 1)
        self.sprite.setSizeScalar(baseSize + factor * 10)

    def update(self, dt):
        worldVector = (self.world.direction[0] * self.world.speed,
                       self.world.direction[1] * self.world.speed)
        worldOffset = (worldVector[0] * self.otcos - worldVector[1] * self.otsin,
                       worldVector[0] * self.otsin - worldVector[1] * self.otcos)

        centerPos = (self.pos[0] + self.velocity[0] + worldOffset[0],
                     self.pos[1] + self.velocity[1] + worldOffset[1])

        if self.isRespawned:
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
