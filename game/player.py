from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *
import math

from sprite import Sprite

SQRT_2_DIV_2 = math.sqrt(2) / 2

TOP_SPEED = 5

class Player():
    def __init__(self, playerCode, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.playerCode = playerCode
        self.frameNum = 0

        self.bottomLeft = (0, 0)
        self.topRight = (700, 500)
        self.pos = (0, 0)

        self.direction = (0, 0)
        self.speed = 0
        self.targetDirection = (0, 0)
        self.targetSpeed = 0
        self.isTweeningDirection = False
        self.isTweeningSpeed = False
        self.newDirectionSince = 0
        self.newSpeedSince = 0
        self.directionChange = (0, 0)

        if playerCode == 'p2':
        	self.sprite.color.r = 1

        if playerCode == 'enemy1':
        	self.sprite.color.b = 1

        self.canvas.add(self.sprite.canvas)

    def reset(self):
        self.frameNum = 0

    def setBounds(self, bottomLeft, topRight):
        self.bottomLeft = bottomLeft
        self.topRight = topRight

    def setCenterPos(self, centerPos):
    	self.pos = centerPos
        self.sprite.setCenterPos(self.pos)

    def setPlayerKeyReport(self, playerKeyReport):
        self.playerKeyReport = playerKeyReport

    def update(self, dt):
        self.frameNum += 1
        self.updateDynamics()
        self.updateTweening()
        self.updatePosition()

    def updateDynamics(self):
        dX = 0
        dY = 0
        scale = 1
        speed = 0

        if self.playerKeyReport.up:
            dY = 1
        elif self.playerKeyReport.down:
            dY = -1

        if self.playerKeyReport.left:
            dX = -1
        elif self.playerKeyReport.right:
            dX = 1

        if not dY == 0 and not dX == 0:
            scale = SQRT_2_DIV_2

        if not dY == 0 or not dX == 0:
            speed = TOP_SPEED

        targetDirection = (dX * scale, dY * scale)
        wasNullDirection = (self.targetDirection[0] == 0 and self.targetDirection[1] == 0)
        isNullDirection = (targetDirection[0] == 0 and targetDirection[1] == 0)
        isNewTargetDirection = (not self.targetDirection[0] == targetDirection[0] or
                                not self.targetDirection[1] == targetDirection[1])
        if not isNullDirection and isNewTargetDirection:
            if wasNullDirection:
                self.targetDirection = targetDirection
                self.direction = targetDirection
            else:
                self.isTweeningDirection = True
                self.newDirectionSince = self.frameNum
                self.targetDirection = targetDirection
                self.calculateDirectionVector()

        isNewTargetSpeed = not self.targetSpeed == speed
        if isNewTargetSpeed:
            self.isTweeningSpeed = True
            self.newSpeedSince = self.frameNum
            self.targetSpeed = speed

    def updateTweening(self):
        self.updateSpeedTweening()
        self.accountForZeroSpeed()
        self.updateDirectionTweening()

    def updateSpeedTweening(self):
        if not self.isTweeningSpeed:
            return

        speedDelta = 1
        speedDirection = 1
        speedTweeningContinues = True
        if self.targetSpeed < self.speed:
            speedDirection = -1

        nextSpeed = self.speed + speedDirection * speedDelta
        if speedDirection == -1 and nextSpeed < self.targetSpeed:
            nextSpeed = self.targetSpeed
            speedTweeningContinues = False
        elif speedDirection == 1 and nextSpeed > self.targetSpeed:
            nextSpeed = self.targetSpeed
            speedTweeningContinues = False

        self.speed = nextSpeed
        self.isTweeningSpeed = speedTweeningContinues

    def accountForZeroSpeed(self):
        if self.speed == 0:
            self.isTweeningDirection = False
            self.targetDirection = (0, 0)
            self.direction = (0, 0)

    def calculateDirectionVector(self):
        subdivs = 5
        vector = (self.targetDirection[0] - self.direction[0],
                  self.targetDirection[1] - self.direction[1])
        vectorLength = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
        self.directionChange = (vector[0] / (vectorLength * subdivs),
                                vector[1] / (vectorLength * subdivs))


    def updateDirectionTweening(self):
        if not self.isTweeningDirection:
            return

        nextDirection = self.direction
        directionTweeningContinues = True

        nextDirection = (self.direction[0] + self.directionChange[0],
                         self.direction[1] + self.directionChange[1])
        remainder = (nextDirection[0] - self.targetDirection[0],
                     nextDirection[1] - self.targetDirection[1])
        targetDirectionLen = math.sqrt(math.pow(self.targetDirection[0], 2) +
                                       math.pow(self.targetDirection[1], 2))
        # "unrotate" the remainder by the target direction so we
        # can compare distance along that line.
        if False:
            dotA = self.targetDirection[0] * remainder[0] / targetDirectionLen
            dotB = self.targetDirection[1] * remainder[1] / targetDirectionLen
            dot = dotA + dotB
            didOvershoot = (dot < 0)

        ## Check if we went out of the unit circle
        len = math.pow(nextDirection[0], 2) + math.pow(nextDirection[1], 2)
        didOvershoot = len > 1

        if didOvershoot:
            nextDirection = self.targetDirection
            directionTweeningContinues = False


        self.direction = nextDirection
        self.isTweeningDirection = directionTweeningContinues


    def updatePosition(self):
        if self.speed <= 0.001:
            return

        len = math.sqrt(math.pow(self.direction[0], 2) + math.pow(self.direction[1], 2))
        if len == 0:
            return
        newCoords = (self.pos[0] + self.direction[0] * self.speed / len,
                     self.pos[1] + self.direction[1] * self.speed / len)

        self.setCenterPos(newCoords)
