#  This script includes two dictionaries containing mappings for the windows virtual key codes
#  The motivation was getting access to keycodes that the don't appear to be included
#  with the win32con.VK_* constants, and lacked Constant names
#  (So VK_SHIFT would be in win32con, but I'm not sure 'A key' would be)
#  Missing are values that the online documentation grouped under common labels or were reserved
#  All mappings come from the online MDSN documentation, with the exception of the
#  ALT keys, which have been renamed from the HOME keys for readability.

keycode2description = {
    1: "Left mouse button",
    2: "Right mouse button",
    3: "Control-break processing",
    4: "Middle mouse button",
    5: "X1 mouse button",
    6: "X2 mouse button",
    7: "Undefined",
    8: "BACKSPACE key",
    9: "TAB key",
    12: "CLEAR key",
    13: "ENTER key",
    16: "SHIFT key",
    17: "CTRL key",
    18: "Undefined",
    19: "PAUSE key",
    20: "CAPS LOCK key",
    21: "IME Hangul mode",
    22: "Undefined",
    23: "IME Junja mode",
    24: "IME final mode",
    25: "IME Kanji mode",
    26: "Undefined",
    27: "ESC key",
    28: "IME convert",
    29: "IME nonconvert",
    30: "IME accept",
    31: "IME mode change request",
    32: "SPACEBAR",
    33: "PAGE UP key",
    34: "PAGE DOWN key",
    35: "END key",
    36: "HOME key",
    37: "LEFT ARROW key",
    38: "UP ARROW key",
    39: "RIGHT ARROW key",
    40: "DOWN ARROW key",
    41: "SELECT key",
    42: "PRINT key",
    43: "EXECUTE key",
    44: "PRINT SCREEN key",
    45: "INS key",
    46: "DEL key",
    47: "HELP key",
    48: "0 key",
    49: "1 key",
    50: "2 key",
    51: "3 key",
    52: "4 key",
    53: "5 key",
    54: "6 key",
    55: "7 key",
    56: "8 key",
    57: "9 key",
    65: "A key",
    66: "B key",
    67: "C key",
    68: "D key",
    69: "E key",
    70: "F key",
    71: "G key",
    72: "H key",
    73: "I key",
    74: "J key",
    75: "K key",
    76: "L key",
    77: "M key",
    78: "N key",
    79: "O key",
    80: "P key",
    81: "Q key",
    82: "R key",
    83: "S key",
    84: "T key",
    85: "U key",
    86: "V key",
    87: "W key",
    88: "X key",
    89: "Y key",
    90: "Z key",
    91: "Left Windows key (Natural keyboard)",
    92: "Right Windows key (Natural keyboard)",
    93: "Applications key (Natural keyboard)",
    94: "Reserved",
    95: "Computer Sleep key",
    96: "Numeric keypad 0 key",
    97: "Numeric keypad 1 key",
    98: "Numeric keypad 2 key",
    99: "Numeric keypad 3 key",
    100: "Numeric keypad 4 key",
    101: "Numeric keypad 5 key",
    102: "Numeric keypad 6 key",
    103: "Numeric keypad 7 key",
    104: "Numeric keypad 8 key",
    105: "Numeric keypad 9 key",
    106: "Multiply key",
    107: "Add key",
    108: "Separator key",
    109: "Subtract key",
    110: "Decimal key",
    111: "Divide key",
    112: "F1 key",
    113: "F2 key",
    114: "F3 key",
    115: "F4 key",
    116: "F5 key",
    117: "F6 key",
    118: "F7 key",
    119: "F8 key",
    120: "F9 key",
    121: "F10 key",
    122: "F11 key",
    123: "F12 key",
    124: "F13 key",
    125: "F14 key",
    126: "F15 key",
    127: "F16 key",
    128: "F17 key",
    129: "F18 key",
    130: "F19 key",
    131: "F20 key",
    132: "F21 key",
    133: "F22 key",
    134: "F23 key",
    135: "F24 key",
    144: "NUM LOCK key",
    145: "SCROLL LOCK key",
    160: "Left SHIFT key",
    161: "Right SHIFT key",
    162: "Left CONTROL key",
    163: "Right CONTROL key",
    164: "Left ALT key",
    165: "Right ALT key",
    166: "Browser Back key",
    167: "Browser Forward key",
    168: "Browser Refresh key",
    169: "Browser Stop key",
    170: "Browser Search key",
    171: "Browser Favorites key",
    172: "Browser Start and Home key",
    173: "Volume Mute key",
    174: "Volume Down key",
    175: "Volume Up key",
    176: "Next Track key",
    177: "Previous Track key",
    178: "Stop Media key",
    179: "Play/Pause Media key",
    180: "Start Mail key",
    181: "Select Media key",
    182: "Start Application 1 key",
    183: "Start Application 2 key",
    186: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ';:' key",
    187: "For any country/region, the '+' key",
    188: "For any country/region, the ',' key",
    189: "For any country/region, the '-' key",
    190: "For any country/region, the '.' key",
    191: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '/?' key",
    192: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '`~' key",
    219: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '[{' key",
    220: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '\|' key",
    221: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ']}' key",
    222: "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the 'single-quote/double-quote' key",
    223: "Used for miscellaneous characters; it can vary by keyboard.",
    224: "Reserved",
    225: "OEM specific",
    226: "Either the angle bracket key or the backslash key on the RT 102-key keyboard",
    229: "IME PROCESS key",
    230: "OEM specific",
    231: "Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in *KEYBDINPUT*, *SendInput*, *WM_KEYDOWN*, and *WM_KEYUP*",
    232: "Unassigned",
    246: "Attn key",
    247: "CrSel key",
    248: "ExSel key",
    249: "Erase EOF key",
    250: "Play key",
    251: "Zoom key",
    252: "Reserved",
    253: "PA1 key",
    254: "Clear key"}

description2keycode = {
    "Left mouse button": 1,
    "Right mouse button": 2,
    "Control-break processing": 3,
    "Middle mouse button (three-button mouse)": 4,
    "X1 mouse button": 5,
    "X2 mouse button": 6,
    "Undefined": 18,
    "BACKSPACE key": 8,
    "TAB key": 9,
    "CLEAR key": 12,
    "ENTER key": 13,
    "SHIFT key": 16,
    "CTRL key": 17,
    "ALT key": 18,
    "PAUSE key": 19,
    "CAPS LOCK key": 20,
    "IME Kana mode": 21,
    "IME Hanguel mode (maintained for compatibility; use *VK_HANGUL*)": 21,
    "IME Hangul mode": 21,
    "IME Junja mode": 23,
    "IME final mode": 24,
    "IME Hanja mode": 25,
    "IME Kanji mode": 25,
    "ESC key": 27,
    "IME convert": 28,
    "IME nonconvert": 29,
    "IME accept": 30,
    "IME mode change request": 31,
    "SPACEBAR": 32,
    "PAGE UP key": 33,
    "PAGE DOWN key": 34,
    "END key": 35,
    "HOME key": 36,
    "LEFT ARROW key": 37,
    "UP ARROW key": 38,
    "RIGHT ARROW key": 39,
    "DOWN ARROW key": 40,
    "SELECT key": 41,
    "PRINT key": 42,
    "EXECUTE key": 43,
    "PRINT SCREEN key": 44,
    "INS key": 45,
    "DEL key": 46,
    "HELP key": 47,
    "0 key": 48,
    "1 key": 49,
    "2 key": 50,
    "3 key": 51,
    "4 key": 52,
    "5 key": 53,
    "6 key": 54,
    "7 key": 55,
    "8 key": 56,
    "9 key": 57,
    "A key": 65,
    "B key": 66,
    "C key": 67,
    "D key": 68,
    "E key": 69,
    "F key": 70,
    "G key": 71,
    "H key": 72,
    "I key": 73,
    "J key": 74,
    "K key": 75,
    "L key": 76,
    "M key": 77,
    "N key": 78,
    "O key": 79,
    "P key": 80,
    "Q key": 81,
    "R key": 82,
    "S key": 83,
    "T key": 84,
    "U key": 85,
    "V key": 86,
    "W key": 87,
    "X key": 88,
    "Y key": 89,
    "Z key": 90,
    "Left Windows key (Natural keyboard)": 91,
    "Right Windows key (Natural keyboard)": 92,
    "Applications key (Natural keyboard)": 93,
    "Reserved": 252,
    "Computer Sleep key": 95,
    "Numeric keypad 0 key": 96,
    "Numeric keypad 1 key": 97,
    "Numeric keypad 2 key": 98,
    "Numeric keypad 3 key": 99,
    "Numeric keypad 4 key": 100,
    "Numeric keypad 5 key": 101,
    "Numeric keypad 6 key": 102,
    "Numeric keypad 7 key": 103,
    "Numeric keypad 8 key": 104,
    "Numeric keypad 9 key": 105,
    "Multiply key": 106,
    "Add key": 107,
    "Separator key": 108,
    "Subtract key": 109,
    "Decimal key": 110,
    "Divide key": 111,
    "F1 key": 112,
    "F2 key": 113,
    "F3 key": 114,
    "F4 key": 115,
    "F5 key": 116,
    "F6 key": 117,
    "F7 key": 118,
    "F8 key": 119,
    "F9 key": 120,
    "F10 key": 121,
    "F11 key": 122,
    "F12 key": 123,
    "F13 key": 124,
    "F14 key": 125,
    "F15 key": 126,
    "F16 key": 127,
    "F17 key": 128,
    "F18 key": 129,
    "F19 key": 130,
    "F20 key": 131,
    "F21 key": 132,
    "F22 key": 133,
    "F23 key": 134,
    "F24 key": 135,
    "NUM LOCK key": 144,
    "SCROLL LOCK key": 145,
    "Left SHIFT key": 160,
    "Right SHIFT key": 161,
    "Left CONTROL key": 162,
    "Right CONTROL key": 163,
    "Left ALT key": 164,
    "Right ALT key": 165,
    "Browser Back key": 166,
    "Browser Forward key": 167,
    "Browser Refresh key": 168,
    "Browser Stop key": 169,
    "Browser Search key": 170,
    "Browser Favorites key": 171,
    "Browser Start and Home key": 172,
    "Volume Mute key": 173,
    "Volume Down key": 174,
    "Volume Up key": 175,
    "Next Track key": 176,
    "Previous Track key": 177,
    "Stop Media key": 178,
    "Play/Pause Media key": 179,
    "Start Mail key": 180,
    "Select Media key": 181,
    "Start Application 1 key": 182,
    "Start Application 2 key": 183,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ';:' key": 186,
    "For any country/region, the '+' key": 187,
    "For any country/region, the ',' key": 188,
    "For any country/region, the '-' key": 189,
    "For any country/region, the '.' key": 190,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '/?' key": 191,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '`~' key": 192,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '[{' key": 219,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '\|' key": 220,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ']}' key": 221,
    "Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the 'single-quote/double-quote' key": 222,
    "Used for miscellaneous characters; it can vary by keyboard.": 223,
    "OEM specific": 230,
    "Either the angle bracket key or the backslash key on the RT 102-key keyboard": 226,
    "IME PROCESS key": 229,
    "Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in *KEYBDINPUT*, *SendInput*, *WM_KEYDOWN*, and *WM_KEYUP*": 231,
    "Unassigned": 232,
    "Attn key": 246,
    "CrSel key": 247,
    "ExSel key": 248,
    "Erase EOF key": 249,
    "Play key": 250,
    "Zoom key": 251,
    "PA1 key": 253,
    "Clear key": 254}
