
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.label import Label
import random

from player import Player
from beam import Beam
from enemy import Enemy

class PlayWidget(Widget):

    score = 0
    enemies = []
    player1 = None
    player2 = None

    def __init__(self, **kwargs):
        super(PlayWidget, self).__init__(**kwargs)

        # 330, 220
        playRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.canvas.add(Color(0.2, 0.2, 0.2))
        self.canvas.add(playRect)

        # Create Players
        self.player1 = Player('p1')
        self.player1.setCenterPos((330, 220))
        self.canvas.add(self.player1.canvas)

        self.player2 = Player('p2')
        self.player2.setCenterPos((230, 120))
        self.canvas.add(self.player2.canvas)

        # Create Beam
        self.beam = Beam(self.player1, self.player2)
        self.canvas.add(self.beam.canvas)

        # Create Enemies
        for x in range(0, 5):
            enemy = Enemy()
            enemy.randomPosition()
            self.enemies.append(enemy)
            self.canvas.add(enemy.canvas)

        # Create Score Label
        self.scoreLabel = Label(text='Score: ' + str(self.score), pos=(295, 400))
        self.canvas.add(self.scoreLabel.canvas)

        self.frameNum = 0
        self.shouldClose = False

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.beam.setKeyReport(keyReport)

    def reset(self):
        self.frameNum = 0

    def update(self, dt):
        self.frameNum += 1

        # Update Players
        self.player1.update(dt)
        self.player2.update(dt)

        # Update Beam
        self.beam.update(dt)

        # Update Enemies
        for enemy in self.enemies:
            enemy.update(dt)

        # If beam is fireing
            # Grab beam coords
            # Iterate through enemies
                # if enemy is in collision with beam, score++

            # Iterate through power-ups
                # if power-up is in collision with beam
                    # Remove power-up
                    # score -= 10


