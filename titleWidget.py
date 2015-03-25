
from kivy.uix.widget import Widget
from kivy.graphics import *

class TitleWidget(Widget):

    def __init__(self, **kwargs):
        super(TitleWidget, self).__init__(**kwargs)

        titleRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.5, 0.5, 0.5))
        self.canvas.add(titleRect)
