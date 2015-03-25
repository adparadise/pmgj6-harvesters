from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *

from sprite import Sprite

class Player():
    def __init__(self, playerCode, **kwargs):
        self.canvas = InstructionGroup()

        self.sprite = Sprite()

        self.playerCode = playerCode

        self.pos = (0, 0)

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
    	else:
	        if self.keyReport.p2_up:
	            dY = speed
	            anyChange = True
	        elif self.keyReport.p2_down:
	            dY = -speed
	            anyChange = True

	        if self.keyReport.p2_left:
	            dX = -speed
	            anyChange = True
	        elif self.keyReport.p2_right:
	            dX = speed
	            anyChange = True

        if anyChange:
            self.setCenterPos((self.pos[0] + dX, self.pos[1] + dY))
