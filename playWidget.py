
from kivy.uix.widget import Widget
from kivy.graphics import *

from beam import Beam


class PlayWidget(Widget):

    def __init__(self, **kwargs):
        super(PlayWidget, self).__init__(**kwargs)

        # 330, 220
        playRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.2, 0.2, 0.2))
        self.canvas.add(playRect)

        self.beam = Beam()
        self.canvas.add(self.beam.canvas)

        self.frameNum = 0

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.beam.setKeyReport(keyReport)

    def reset(self):
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1
        self.beam.update(dt)
