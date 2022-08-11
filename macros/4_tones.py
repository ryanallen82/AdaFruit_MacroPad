# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'B Flat minor', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x2e2a5d, 'Bf3', [{'tone':233.08}]),
        (0x2e2a5d, 'C4', [{'tone':261.63}]),
        (0x2e2a5d, 'Df4', [{'tone':277.18}]),
        # 2nd row ----------
        (0x2e2a5d, 'Ef4', [{'tone':311.13}]),
        (0x2e2a5d, 'F4', [{'tone':349.23}]),
        (0x2e2a5d, 'Gf4', [{'tone':369.99}]),
        # 3rd row ----------
        (0x2e2a5d, 'Af4', [{'tone':415.30}]),
        (0x2e2a5d, 'Bf4', [{'tone':466.16}]),
        (0x2e2a5d, 'C5', [{'tone':523.25}]),
        # 4th row ----------
        (0x2e2a5d, 'Df5', [{'tone':554.37}]),
        (0x2e2a5d, 'Ef5', [{'tone':622.25}]),
        (0x2e2a5d, 'F5', [{'tone':698.46}]),
        # Encoder button ---
        (0x2e2a5d, '', [])
    ]
}
