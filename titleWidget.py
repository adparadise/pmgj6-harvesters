
from kivy.uix.widget import Widget
from kivy.graphics import *

class TitleWidget(Widget):

    def __init__(self, **kwargs):
        super(TitleWidget, self).__init__(**kwargs)

        titleRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.5, 0.5, 0.5))
        self.canvas.add(titleRect)
        self.shouldClose = False
        self.keyReport = None

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport

    def cleanup(self):
        pass

    def reset(self):
        self.shouldClose = False
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1
        if (self.frameNum > 60 and
            self.keyReport.player1.button1 or self.keyReport.player1.button2 or
            self.keyReport.player2.button1 or self.keyReport.player2.button2):
            self.shouldClose = True
