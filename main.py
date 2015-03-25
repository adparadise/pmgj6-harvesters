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


class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.title = TitleWidget()
        self.play = PlayWidget()

        self.showTitle()

    def showGame(self):
        self.remove_widget(self.title)
        self.add_widget(self.play)
        self.isTitle = False

    def showTitle(self):
        self.remove_widget(self.play)
        self.add_widget(self.title)
        self.isTitle = True

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[0] == 114:
            pass

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[0] == 114:
            if self.isTitle:
                self.showGame()
            else:
                self.showTitle()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def update(self, dt):
        pass

class MainApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    MainApp().run()

