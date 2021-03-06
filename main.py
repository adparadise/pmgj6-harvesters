#!/usr/bin/python

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'system')

import kivy
import math
kivy.require('1.0.8')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

from titleWidget import TitleWidget
from playWidget import PlayWidget

from keyReport import KeyReport


class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.keyReport = KeyReport()

        self.title = TitleWidget()
        self.title.setKeyReport(self.keyReport)
        self.play = PlayWidget()
        self.play.setKeyReport(self.keyReport)
        self.currentWidget = None


        self.frameNum = 0
        self.currentWidgetStartFrameNum = 0

        self.showWidget(self.title)

    def showWidget(self, widget):
        if not self.currentWidget == None:
            self.remove_widget(self.currentWidget)
            self.currentWidget.cleanup()

        if widget == self.title:
            widget.setLastScore(self.play.score)

        self.currentWidget = widget
        self.currentWidget.reset()
        self.currentWidgetStartFrameNum = self.frameNum
        self.add_widget(self.currentWidget)

    def showNextWidget(self):
        if self.currentWidget == None:
            self.showWidget(self.title)
        elif self.currentWidget == self.title:
            self.showWidget(self.play)
        elif self.currentWidget == self.play:
            self.showWidget(self.title)



    def _on_keyboard_up(self, keyboard, keycode):
        self.keyReport.keyUp(keycode[0])

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.keyReport.keyDown(keycode[0])

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def update(self, dt):
        if self.currentWidget == None:
            return

        self.frameNum += 1
        self.currentWidget.update(dt)
        if self.currentWidget.shouldClose:
            self.showNextWidget()

class MainApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    MainApp().run()

