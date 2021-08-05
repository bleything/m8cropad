from rainbowio import colorwheel
from adafruit_hid.keycode import Keycode

COLOR_CODES = {
    "red":    colorwheel(0),
    "orange": colorwheel(12),
    "green":  colorwheel(72),
    "blue":   colorwheel(170),
    "yellow": colorwheel(28),
    "cyan":   colorwheel(120),
    "purple": colorwheel(196),
    "pink":   colorwheel(230),
}

ORIENTATIONS = {
    "UP": {
        "angle": 0,
        "orientation": "vertical"
    },

    "DOWN": {
        "angle": 180,
        "orientation": "vertical"
    },

    "LEFT": {
        "angle": 90,
        "orientation": "horizontal"
    },

    "RIGHT": {
        "angle": 270,
        "orientation": "horizontal"
    }
}

KEY_CONFIG = {
    "up": {
        "color": "arrows",
        "code": Keycode.UP_ARROW,

        "key": {
            "horizontal": 1,
            "vertical": 4,
        }
    },

    "down": {
        "color": "arrows",
        "code": Keycode.DOWN_ARROW,

        "key": {
            "horizontal": 5,
            "vertical": 7,
        }
    },

    "left": {
        "color": "arrows",
        "code": Keycode.LEFT_ARROW,

        "key": {
            "horizontal": 4,
            "vertical": 6,
        }
    },

    "right": {
        "color": "arrows",
        "code": Keycode.RIGHT_ARROW,

        "key": {
            "horizontal": 6,
            "vertical": 8,
        }
    },

    ### function keys

    "opt": {
        "color": "function",
        "code": Keycode.Z,

        "key": {
            "horizontal": 2,
            "vertical": 1,
        }
    },

    "edit": {
        "color": "function",
        "code": Keycode.X,

        "key": {
            "horizontal": 3,
            "vertical": 2,
        }
    },

    "shift": {
        "color": "shift",
        "code": Keycode.LEFT_SHIFT,

        "key": {
            "horizontal": 9,
            "vertical": 10,
        }
    },

    "play": {
        "color": "play",
        "code": Keycode.SPACEBAR,

        "key": {
            "horizontal": 10,
            "vertical": 11,
        }
    },
}
