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
	p1_down = 0
	p1_up = 0
	p1_left = 0
	p1_right = 0
	p1_button1 = 0
	p1_button2 = 0

	p2_down = 0
	p2_up = 0
	p2_left = 0
	p2_right = 0
	p2_button1 = 0
	p2_button2 = 0

	def keyUp(self, keycode):
		if keycode == 308:
			p1_button1 = 1
		elif keycode == 305:
			p1_button2 = 1
		elif keycode == 275:
			p1_right = 1
		elif keycode == 276:
			p1_left = 1
		elif keycode == 274:
			p1_down = 1
		elif keycode == 273:
			p1_up = 1
		elif keycode == 114:
			p2_up = 1
		elif keycode == 102:
			p1_down = 1
		elif keycode == 100:
			p1_left = 1
		elif keycode == 103:
			p1_right = 1
		elif keycode == 87:
			p1_button1 = 1
		elif keycode == 115:
			p1_button2 = 1

	def keyDown(self, keycode):
		if keycode == 308:
			p1_button1 = 0
		elif keycode == 305:
			p1_button2 = 0
		elif keycode == 275:
			p1_right = 0
		elif keycode == 276:
			p1_left = 0
		elif keycode == 274:
			p1_down = 0
		elif keycode == 273:
			p1_up = 0
		elif keycode == 114:
			p2_up = 0
		elif keycode == 102:
			p1_down = 0
		elif keycode == 100:
			p1_left = 0
		elif keycode == 103:
			p1_right = 0
		elif keycode == 87:
			p1_button1 = 0
		elif keycode == 115:
			p1_button2 = 0
