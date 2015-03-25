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

class KeyReport(object):
	p1_down = False
	p1_up = False
	p1_left = False
	p1_right = False
	p1_button1 = False
	p1_button2 = False

	p2_down = False
	p2_up = False
	p2_left = False
	p2_right = False
	p2_button1 = False
	p2_button2 = False

	def keyUp(self, keycode):
		if keycode == 308:
			p1_button1 = True
		elif keycode == 305:
			p1_button2 = True
		elif keycode == 275:
			p1_right = True
		elif keycode == 276:
			p1_left = True
		elif keycode == 274:
			p1_down = True
		elif keycode == 273:
			p1_up = True
		elif keycode == 114:
			p2_up = True
		elif keycode == 102:
			p1_down = True
		elif keycode == 100:
			p1_left = True
		elif keycode == 103:
			p1_right = True
		elif keycode == 87:
			p1_button1 = True
		elif keycode == 115:
			p1_button2 = True

	def keyDown(self, keycode):
		if keycode == 308:
			p1_button1 = False
		elif keycode == 305:
			p1_button2 = False
		elif keycode == 275:
			p1_right = False
		elif keycode == 276:
			p1_left = False
		elif keycode == 274:
			p1_down = False
		elif keycode == 273:
			p1_up = False
		elif keycode == 114:
			p2_up = False
		elif keycode == 102:
			p1_down = False
		elif keycode == 100:
			p1_left = False
		elif keycode == 103:
			p1_right = False
		elif keycode == 87:
			p1_button1 = False
		elif keycode == 115:
			p1_button2 = False
