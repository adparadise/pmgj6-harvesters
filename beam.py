from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *

from player import Player

class Beam():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.player1Pos = (330, 220)
        self.player1 = Player()
        self.player1.setCenterPos(self.player1Pos)

        self.canvas.add(self.player1.canvas)

    def setCenterPos(self, centerPos):
    	pass

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport

    def update(self, dt):
        dX = 0
        dY = 0
        speed = 10
        anyChange = False
        if self.keyReport.p1_up:
            dY = speed
            anyChange = True
        elif self.keyReport.p1_down:
            dY = -speed
            anyChange = True

        if self.keyReport.p1_left:
            dX = -speed
            anyChange = True
        elif self.keyReport.p1_right:
            dX = speed
            anyChange = True

        if anyChange:
            self.player1Pos = (self.player1Pos[0] + dX,
                               self.player1Pos[1] + dY)
            self.player1.setCenterPos(self.player1Pos)
