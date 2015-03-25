
from kivy.uix.widget import Widget
from kivy.graphics import *

class PlayWidget(Widget):

    def __init__(self, **kwargs):
        super(PlayWidget, self).__init__(**kwargs)

        playRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.2, 0.2, 0.2))
        self.canvas.add(playRect)
        self.frameNum = 0

    def reset(self):
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1
