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


class Player(object):
    down = False
    up = False
    left = False
    right = False

    button1 = False
    button2 = False

class KeyReport(object):
    player1 = Player()
    player2 = Player()

    def keyUp(self, keycode):
        if keycode == 308:
            self.player1.button1 = False
        elif keycode == 305:
            self.player1.button2 = False
        elif keycode == 275:
            self.player1.right = False
        elif keycode == 276:
            self.player1.left = False
        elif keycode == 274:
            self.player1.down = False
        elif keycode == 273:
            self.player1.up = False
        elif keycode == 114:
            self.player2.up = False
        elif keycode == 102:
            self.player2.down = False
        elif keycode == 100:
            self.player2.left = False
        elif keycode == 103:
            self.player2.right = False
        elif keycode == 115:
            self.player2.button1 = False
        elif keycode == 97:
            self.player2.button2 = False

    def keyDown(self, keycode):
        if keycode == 308:
            self.player1.button1 = True
        elif keycode == 305:
            self.player1.button2 = True
        elif keycode == 275:
            self.player1.right = True
        elif keycode == 276:
            self.player1.left = True
        elif keycode == 274:
            self.player1.down = True
        elif keycode == 273:
            self.player1.up = True
        elif keycode == 114:
            self.player2.up = True
        elif keycode == 102:
            self.player2.down = True
        elif keycode == 100:
            self.player2.left = True
        elif keycode == 103:
            self.player2.right = True
        elif keycode == 115:
            self.player2.button1 = True
        elif keycode == 97:
            self.player2.button2 = True
