
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.label import Label
import math

from game.player import Player
from game.beam import Beam
from game.enemy import Enemy
from game.world import World

FRAMERATE = 60

class PlayWidget(Widget):
    frameNum = 0
    score = 0
    enemies = []
    player1 = None
    player2 = None
    world = None

    roundFrames = FRAMERATE * 10

    def __init__(self, **kwargs):
        super(PlayWidget, self).__init__(**kwargs)

        # 330, 220
        playRect = Rectangle(pos=(50, 40), size=(610, 400))

        self.enemyGroup = InstructionGroup()

        self.world = World()

        # Create Players
        self.player1 = Player('p1')

        self.player2 = Player('p2')

        # Create Beam
        self.beam = Beam(self.player1, self.player2)

        # Create Score Label
        self.scoreLabel = Label(text='', pos=(295, 400))
        self.timerLabel = Label(text='', pos=(560, 350),
                                font_size=100, halign='right')
        self.updateScoreDisplay()
        self.updateTimerDisplay()

        # Background
        self.canvas.add(Color(0.2, 0.2, 0.2))
        #self.canvas.add(playRect)
        self.canvas.add(self.enemyGroup)
        self.canvas.add(self.beam.canvas)
        self.canvas.add(self.player1.canvas)
        self.canvas.add(self.player2.canvas)
        self.canvas.add(self.scoreLabel.canvas)
        self.canvas.add(self.timerLabel.canvas)

        self.timeOfLastSpawn = 0
        self.nextSpawnIn = 0
        self.shouldClose = False

    def setKeyReport(self, keyReport):
        self.keyReport = keyReport
        self.beam.setKeyReport(keyReport)

    def reset(self):
        self.shouldClose = False
        self.frameNum = 0
        self.world.reset()
        self.player1.reset()
        self.player2.reset()
        self.player1.setCenterPos((200, 220))
        self.player2.setCenterPos((460, 220))
        self.score = 0

    def cleanup(self):
        self.enemyGroup.clear()
        self.enemies = []

    def spawnEnemy(self):
        enemy = Enemy()
        enemy.reset(False)
        enemy.setWorld(self.world)
        self.enemyGroup.add(enemy.canvas)

        centerPos = self.world.nextEnemyPos()
        enemy.setCenterPos(centerPos)
        self.enemies.append(enemy)

    def update(self, dt):
        self.frameNum += 1

        if self.frameNum > self.roundFrames:
            self.shouldClose = True
            return

        if self.frameNum % FRAMERATE == 0:
            self.updateTimerDisplay()

        self.world.update(dt)

        # Update Players
        self.player1.update(dt)
        self.player2.update(dt)

        self.spawnNewEnemies()

        # Update Enemies
        for enemy in self.enemies:
            enemy.update(dt)

        if self.beam.beamState == 0:
            self.beam.setIsColliding(False)
        else:
            collisions = self.getCollisions()
            if len(collisions) > 0:
                self.beam.setIsColliding(True)
                self.consumeEnemies(collisions, self.beam.beamState)
            else:
                self.beam.setIsColliding(False)

        self.clearDeadEnemies()

        # Update Beam
        self.beam.update(dt)

    def consumeEnemies(self, collisions, beamState):
        totalDelta = 0
        for enemy in collisions:
            delta = enemy.decrement(beamState)
            totalDelta += delta

        if not totalDelta == 0:
            self.score += totalDelta
            self.updateScoreDisplay()

    def updateScoreDisplay(self):
        self.scoreLabel.text = 'Score: ' + str(self.score)

    def updateTimerDisplay(self):
        seconds = int(math.ceil((self.roundFrames - self.frameNum) / FRAMERATE))
        if seconds > 5:
            self.timerLabel.color[3] = 0.3
        else:
            self.timerLabel.color[3] = 1
        if seconds > 3:
            self.timerLabel.color[0] = 1
            self.timerLabel.color[1] = 1
            self.timerLabel.color[2] = 1
        else:
            self.timerLabel.color[0] = 0.6
            self.timerLabel.color[1] = 0
            self.timerLabel.color[2] = 0

        self.timerLabel.text = str(seconds)

    def spawnNewEnemies(self):
        if self.timeOfLastSpawn + self.nextSpawnIn > self.frameNum:
            return

        self.spawnEnemy()
        self.timeOfLastSpawn = self.frameNum

        if self.frameNum < 200:
            self.nextSpawnIn = 10


    def clearDeadEnemies(self):
        deadEnemies = []

        for enemy in self.enemies:
            if enemy.shouldRemove:
                deadEnemies.append(enemy)

        if len(deadEnemies) == 0:
            return

        aliveEnemies = []
        for enemy in self.enemies:
            if not enemy.shouldRemove:
                aliveEnemies.append(enemy)

        # rebuild
        self.enemyGroup.clear()
        for enemy in aliveEnemies:
            self.enemyGroup.add(enemy.canvas)

        self.enemies = aliveEnemies


    def getCollisions(self):
        beamLineCoords = (self.player2.pos[0], self.player2.pos[1], self.player1.pos[0], self.player1.pos[1])
        collisions = []

        for enemy in self.enemies:
            if enemy.sprite.collidesWithLine(beamLineCoords):
                collisions.append(enemy)

        return collisions

