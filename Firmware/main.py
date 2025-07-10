import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.SCL, board.TX, board.RX, board.SCK, board.MISO, board.MOSI]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

macros.macros = [
    Tap(['.']),
    Tap(['?']),
    Tap([',']),
    Tap(['!']),
    Tap([';']), 
    Tap([':']),
]

keyboard.keymap = [
    [KC.MACRO_0, KC.MACRO_1, KC.MACRO_2, KC.MACRO_3, KC.MACRO_4, KC.MACRO_5]
]

if __name__ == '__main__':
    keyboard.go()