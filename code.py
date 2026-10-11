import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, SSD1322

kb = KMKKeyboard()
kb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5)
kb.row_pins = (board.GP6, board.GP7, board.GP8)
kb.diode_orientation = DiodeOrientation.COL2ROW
enc = EncoderHandler()
enc.pins = ((board.GP10, board.GP11, board.GP12, False),)
enc.map = (((KC.VOLU,KC.VOLD, KC.MUTE),),)
kb.modules.append(enc)

disp = Display(
    display=SSD1322,
    scl=board.GP18,
    sda=board.GP19,
    cs=board.GP17,
    dc=board.GP16,
    rst=board.GP15
)
kb.extensions.append(disp)
kb.keymap = [
    [
        KC.KP_7,KC.KP_8,KC.KP_9,KC.KP_DOT,
        KC.KP_4,KC.KP_5,KC.KP_6,KC.KP_0,
        KC.KP_1,KC.KP_2,KC.KP_3,KC.KP_ENTER,
    ]
]

if __name__ == '__main__':
    kb.go()