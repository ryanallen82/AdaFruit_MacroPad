from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Function Keys', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xff6700, 'F1', [Keycode.F1]),
        (0xff6700, 'F2', [Keycode.F2]),
        (0xff6700, 'F3', [Keycode.F3]),
        # 2nd row ----------
        (0xff6700, 'F4', [Keycode.F4]),
        (0xff6700, 'F5', [Keycode.F5]),
        (0xff6700, 'F6', [Keycode.F6]),
        # 3rd row ----------
        (0xff6700, 'F7', [Keycode.F7]),
        (0xff6700, 'F8', [Keycode.F8]),
        (0xff6700, 'F9', [Keycode.F9]),
        # 4th row ----------
        (0xff6700, 'F10', [Keycode.F10]),
        (0xff6700, 'F11', [Keycode.F11]),
        (0xff6700, 'F12', [Keycode.F12]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}