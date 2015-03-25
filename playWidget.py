
from kivy.uix.widget import Widget
from kivy.graphics import *

from player import Player

class PlayWidget(Widget):

    def __init__(self, **kwargs):
        super(PlayWidget, self).__init__(**kwargs)

        # 330, 220
        playRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.2, 0.2, 0.2))
        self.canvas.add(playRect)

        self.player1Pos = (330, 220)
        self.player1 = Player()
        self.player1.setCenterPos(self.player1Pos)
        self.canvas.add(self.player1.canvas)

        self.frameNum = 0

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport

    def reset(self):
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1
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
