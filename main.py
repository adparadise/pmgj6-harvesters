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

from title import Title


class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.main = Title()
        self.add_widget(self.main)

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[0] == 114:
            self.isPlayingRequested = False

#define KEY_CODE_LEFT_ALT   0x04    308
#define KEY_CODE_LEFT_CTRL  0x01    305
#define KEY_CODE_RIGHT_ARROW    0x4f    275
#define KEY_CODE_LEFT_ARROW 0x50        276
#define KEY_CODE_DOWN_ARROW 0x51    274
#define KEY_CODE_UP_ARROW   0x52    273
#define KEY_CODE_R      0x15    114
#define KEY_CODE_F      0x09    102
#define KEY_CODE_D      0x07    100
#define KEY_CODE_G      0x0A    103
#define KEY_CODE_A      0x04    87
#define KEY_CODE_S      0x16    115

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[0] == 114:
            self.isPlayingRequested = True

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

