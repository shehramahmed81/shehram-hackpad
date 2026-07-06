import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Switch matrix pins from KiCad schematic
keyboard.row_pins = (
    board.D0,  # ROW0
    board.D1,  # ROW1
    board.D2,  # ROW2
)

keyboard.col_pins = (
    board.D3,  # COL0
    board.D6,  # COL1
    board.D7,  # COL2
    board.D8,  # COL3
)

# If the keys do not work correctly, change to ROW2COL
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Rotary encoder
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D9, board.D10, None),  # A, B, button pin not used here
)

# counterclockwise = volume down, clockwise = volume up
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())


keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4,
        KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N9, KC.N0, KC.ENT, KC.BSPC,
    ]
]

if __name__ == "__main__":
    keyboard.go()