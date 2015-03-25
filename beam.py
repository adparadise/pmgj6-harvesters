from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *

from player import Player

class Beam():
    def __init__(self, **kwargs):
        self.canvas = InstructionGroup()

        self.player1 = Player('p1')
        self.player1.setCenterPos((330, 220))
        self.canvas.add(self.player1.canvas)

        self.player2 = Player('p2')
        self.player2.setCenterPos((230, 120))
        self.canvas.add(self.player2.canvas)

        self.beamLine = Line(points=(100, 200, 150, 250), width=3)
        self.canvas.add(self.beamLine)



    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.player1.setKeyReport(keyReport)
        self.player2.setKeyReport(keyReport)

    def update(self, dt):
    	self.player1.update(dt)
    	self.player2.update(dt)
    	self.beamLine.points = (self.player2.pos[0], self.player2.pos[1], self.player1.pos[0], self.player1.pos[1])
