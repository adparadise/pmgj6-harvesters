
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.label import Label

class TitleWidget(Widget):

    def __init__(self, **kwargs):
        super(TitleWidget, self).__init__(**kwargs)

        titleRect = Rectangle(pos=(50, 40), size=(610, 400))

        fgColor = [0.3, 0.3, 0.3, 1]
        bgColor = [0.2, 0.2, 0.5, 1]

        titleLabel = Label(text='HARVESTERS', pos=(300, 330),
                           font_size=90, halign='center',
                           color=fgColor,
                           bold=True)

        self.lastScoreLabel = Label(text='', pos=(320, 90),
                                    font_size=30, halign='center',
                                    color=fgColor)
        self.hiScoreLabel = Label(text='', pos=(320, 40),
                                  font_size=30, halign='center',
                                  color=fgColor)


        self.hiScore = 0
        self.lastScore = 0

        self.shouldClose = False
        self.keyReport = None

        self.canvas.add(Color(0.1, 0.1, 0.15))
        self.canvas.add(titleRect)
        self.canvas.add(titleLabel.canvas)
        self.canvas.add(self.hiScoreLabel.canvas)
        self.canvas.add(self.lastScoreLabel.canvas)

    def setLastScore(self, score):
        self.lastScore = score
        if self.lastScore > self.hiScore:
            self.hiScore = self.lastScore
        self.updateScores()

    def updateScores(self):
        self.lastScoreLabel.text = "Score: " + str(self.lastScore)
        self.hiScoreLabel.text = "High Score: " + str(self.hiScore)

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
            (self.keyReport.player1.button1 or self.keyReport.player1.button2 or
             self.keyReport.player2.button1 or self.keyReport.player2.button2)):
            self.shouldClose = True
