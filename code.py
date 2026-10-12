import microcontroller
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

kb = KMKKeyboard()

kb.row_pins = (microcontroller.pin.GPIO2, microcontroller.pin.GPIO3, microcontroller.pin.GPIO4)
kb.col_pins = (microcontroller.pin.GPIO5, microcontroller.pin.GPIO6, microcontroller.pin.GPIO7, microcontroller.pin.GPIO8)
kb.diode_orientation = DiodeOrientation.ROW2COL

e = EncoderHandler()
e.pins = ((microcontroller.pin.GPIO27, microcontroller.pin.GPIO28, microcontroller.pin.GPIO29, False),)
e.map = (((KC.VOLU, KC.VOLD, KC.MUTE),),)
kb.modules.append(e)

# TODO: SH1122 driver KMK doesn't have this one, will fix later
# from kmk.extensions.display import Display, SH1122
# d = Display(
#  display=SH1122,
#  scl=microcontroller.pin.GPIO22,
#  sda=microcontroller.pin.GPIO23,
#  cs=microcontroller.pin.GPIO21,
#  dc=microcontroller.pin.GPIO20,
#  rst=microcontroller.pin.GPIO26
# )
# kb.extensions.append(d)

kb.keymap = [
    [
     KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_DOT,
     KC.KP_4, KC.KP_5,  KC.KP_6, KC.KP_0,
     KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER,
    ]
]

if __name__ == '__main__':
 kb.go()