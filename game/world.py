
import random
import math

SPIN_SPEED = math.pi * 0.001

class World(object):


    def __init__(self, **kwargs):
        self.theta = math.pi * 0.5
        self.speed = 1.5
        self.redirect(0)

        self.frameNum = 0

        self.left = 0
        self.right = 700
        self.top = 450
        self.bottom = 10
        self.width = self.right - self.left
        self.height = self.top - self.bottom

    def reset(self):
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1
        self.redirect(SPIN_SPEED)

    def redirect(self, dtheta):
        self.theta += dtheta
        self.direction = (math.cos(self.theta), math.sin(self.theta))

    def nextEnemyPos(self, theta):
        x = 0
        y = 0
        buffer = 5

        sin = math.sin(theta)
        cos = math.cos(theta)
        orientation = (cos * self.direction[0] - sin * self.direction[1],
                       sin * self.direction[0] - cos * self.direction[1])

        if orientation[0] > 0:
            x = self.left + buffer
        else:
            x = self.right - buffer

        if orientation[1] < 0:
            y = self.top - buffer
        else:
            y = self.bottom + buffer

        dx = abs(orientation[0])
        dy = abs(orientation[1])
        if not dx + dy == 0:
            ratio = dx / (dx + dy)
        else:
            print "here"
            ratio = 0.5

        sample = random.random()
        pos = (0, 0)
        if sample < ratio:
            placement = (sample / ratio)
            y = placement * self.height + self.bottom
        else:
            placement = ((sample - ratio) / (1 - ratio))
            x = placement * self.width + self.left

        pos = (x, y)

        return pos
