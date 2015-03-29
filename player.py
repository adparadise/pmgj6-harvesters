from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
from kivy.vector import *

from sprite import Sprite

class Player():
    def __init__(self, playerCode, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.playerCode = playerCode

        self.pos = (0, 0)

        if playerCode == 'p2':
        	self.sprite.color.r = 1

        if playerCode == 'enemy1':
        	self.sprite.color.b = 1

        self.canvas.add(self.sprite.canvas)

    def setCenterPos(self, centerPos):
    	self.pos = centerPos
        self.sprite.setCenterPos(centerPos)

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport

    def update(self, dt):
        dX = 0
        dY = 0
        speed = 10
        anyChange = False

        if self.playerCode == 'p1':
            if self.keyReport.player1.up:
                dY = speed
                anyChange = True
            elif self.keyReport.player1.down:
                dY = -speed
                anyChange = True

            if self.keyReport.player1.left:
                dX = -speed
                anyChange = True
            elif self.keyReport.player1.right:
                dX = speed
                anyChange = True
        else:
            if self.keyReport.player2.up:
                dY = speed
                anyChange = True
            elif self.keyReport.player2.down:
                dY = -speed
                anyChange = True

            if self.keyReport.player2.left:
                dX = -speed
                anyChange = True
            elif self.keyReport.player2.right:
                dX = speed
                anyChange = True

        newCoords = (self.pos[0] + dX, self.pos[1] + dY)

        if anyChange and Vector.in_bbox(newCoords, (15, 10), (690, 470)):
            self.setCenterPos(newCoords)
