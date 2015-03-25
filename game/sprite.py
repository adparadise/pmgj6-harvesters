from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *

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
        self.rect.pos = (self.centerPos[0] - (size[0] / 2), self.centerPos[1] - (size[1] / 2))
        self.rect.size = size

    def setSizeScalar(self, sizeScalar):
        self.sizeScalar = sizeScalar
        self.repos()

    def setCenterPos(self, centerPos):
        self.centerPos = centerPos
        self.repos()

    def collidesWithLine(self, lineCoords):
        halfWidth = self.rect.size[0] / 2
        halfHeight = self.rect.size[1] / 2

        topLeft = (self.centerPos[0] - halfWidth, self.centerPos[1] + halfHeight)
        topRight = (self.centerPos[0] + halfWidth, self.centerPos[1] + halfHeight)
        bottomLeft = (self.centerPos[0] - halfWidth, self.centerPos[1] - halfHeight)
        bottomRight = (self.centerPos[0] + halfWidth, self.centerPos[1] - halfHeight)

        intersection1 = Vector.segment_intersection(topLeft, bottomRight, (lineCoords[0], lineCoords[1]), (lineCoords[2], lineCoords[3]))
        intersection2 = Vector.segment_intersection(bottomLeft, topRight, (lineCoords[0], lineCoords[1]), (lineCoords[2], lineCoords[3]))

        return True if intersection1 or intersection2 else False

