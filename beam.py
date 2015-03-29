from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import *
import math

from player import Player

class Beam():
    enemies = []
    player1 = None
    player2 = None

    def __init__(self, player1, player2, **kwargs):
        self.canvas = InstructionGroup()

        self.beamColor = Color(0.0, 0.0, 0.0, 1.0)
        self.beamGroup = InstructionGroup()
        self.beamThickness = 40
        self.canvas.add(self.beamColor)
        self.canvas.add(self.beamGroup)

        self.player1 = player1
        self.player2 = player2

        self.beamState = 0

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.player1.setKeyReport(keyReport)
        self.player2.setKeyReport(keyReport)

    def updateBeamState(self):
        bothButton1 = self.keyReport.player1.button1 and self.keyReport.player2.button1
        bothButton2 = self.keyReport.player1.button2 and self.keyReport.player2.button2

        beamState = self.beamState
        if not bothButton1 and not bothButton2:
            beamState = 0
        else:
            beamState = 1

        isChanged = False
        if not beamState == self.beamState:
            isChanged = True
            self.beamState = beamState

    def updateBeam(self, p1Pos, p2Pos):
        xDelta = p2Pos[0] - p1Pos[0]
        yDelta = p2Pos[1] - p1Pos[1]
        distanceSquared = math.pow(xDelta, 2) + math.pow(yDelta, 2)
        theta = math.atan2(yDelta, xDelta)
        distance = math.sqrt(distanceSquared)

        self.beamGroup.clear()
        self.beamGroup.add(PushMatrix())
        self.beamGroup.add(Translate(p1Pos[0], p1Pos[1], 0))
        self.beamGroup.add(Rotate(theta * 180 / math.pi, 0, 0, 1))
        self.beamGroup.add(Scale(distance, self.beamThickness, 1))
        self.beamGroup.add(Rectangle(pos=(0, -0.5), size=(1, 1)))
        self.beamGroup.add(PopMatrix())


    def update(self, dt):

    	beamLineCoords = (self.player2.pos[0], self.player2.pos[1], self.player1.pos[0], self.player1.pos[1])

    	#if self.enemies[0].sprite.collidesWithLine(beamLineCoords):
        #    self.beamThickness = 40
    	#else:
        #    self.beamThickness = 1

        isChanged = self.updateBeamState()
        if isChanged:
            if self.beamState == 0:
                self.beamColor.r = 0.3
                self.beamColor.g = 0.3
                self.beamColor.b = 0.3
                self.beamColor.a = 1
            if self.beamState == 1:
                self.beamColor.r = 0.8
                self.beamColor.g = 0.5
                self.beamColor.b = 0.3
                self.beamColor.a = 1

        self.updateBeam(self.player1.pos, self.player2.pos)


