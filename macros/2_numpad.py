# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x20C20E, '1', ['1']),
        (0x20C20E, '2', ['2']),
        (0x20C20E, '3', ['3']),
        # 2nd row ----------
        (0x20C20E, '4', ['4']),
        (0x20C20E, '5', ['5']),
        (0x20C20E, '6', ['6']),
        # 3rd row ----------
        (0x20C20E, '7', ['7']),
        (0x20C20E, '8', ['8']),
        (0x20C20E, '9', ['9']),
        # 4th row ----------
        (0x20C20E, '*', ['*']),
        (0x20C20E, '0', ['0']),
        (0x20C20E, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
