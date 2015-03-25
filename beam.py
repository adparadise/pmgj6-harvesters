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


    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.player1.setKeyReport(keyReport)
        self.player2.setKeyReport(keyReport)

    def update(self, dt):
    	self.player1.update(dt)
    	self.player2.update(dt)
