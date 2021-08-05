from adafruit_macropad import MacroPad
from adafruit_hid.keycode import Keycode
from rainbowio import colorwheel

################################################################################
### config
################################################################################

COLORS = {
    "red": 0,
    "orange": 12,
    "green": 72,
    "blue": 170,
    "yellow": 28,
    "cyan": 120,
    "purple": 196,
    "pink": 230,
}

COLORS["pressed"] = COLORS["orange"]

KEYS = {
    ### arrows

    1: {
        "name": "up",
        "color": "cyan",
        "code": Keycode.UP_ARROW
    },

    4: {
        "name": "left",
        "color": "cyan",
        "code": Keycode.LEFT_ARROW
    },

    5: {
        "name": "down",
        "color": "cyan",
        "code": Keycode.DOWN_ARROW
    },

    6: {
        "name": "right",
        "color": "cyan",
        "code": Keycode.RIGHT_ARROW
    },

    ### function keys

    2: {
        "name": "opt",
        "color": "purple",
        "code": Keycode.Z
    },

    3: {
        "name": "edit",
        "color": "purple",
        "code": Keycode.X
    },

    ### shift / play

    9: {
        "name": "shift",
        "color": "pink",
        "code": Keycode.LEFT_SHIFT
    },

    10: {
        "name": "play",
        "color": "green",
        "code": Keycode.SPACEBAR
    }
}

def color_number(name):
    return colorwheel(COLORS[name])

macropad = MacroPad(rotation=90)  # create the macropad object, rotate orientation

################################################################################
### LED setup
################################################################################

macropad.pixels.brightness = 0.1
macropad.pixels.fill(0)

for key, config in KEYS.items():
    macropad.pixels[key] = color_number(config['color'])

################################################################################
### display setup
################################################################################

text_lines = macropad.display_text("M8cropad")
text_lines.show()

last_knob_pos = macropad.encoder  # store knob position state

while True:

    key_event = macropad.keys.events.get()  # check for key press or release
    if key_event:
        if key_event.pressed:
            key = key_event.key_number
            text_lines[1].text = "press: {}".format(key)

            try:
                keycode = KEYS[key]["code"]

                macropad.pixels[key] = colorwheel(COLORS["pressed"])
                macropad.keyboard.press(keycode)
            except KeyError:
                # undefined key; move along
                pass

        if key_event.released:
            key = key_event.key_number
            text_lines[1].text = "release: {}".format(key)

            try:
                keycode = KEYS[key]["code"]
                color = KEYS[key]["color"]

                macropad.pixels[key] = color_number(color)
                macropad.keyboard.release(keycode)
            except KeyError:
                # undefined key; move along
                pass

    macropad.encoder_switch_debounced.update()  # check the knob switch for press or release
    # if macropad.encoder_switch_debounced.pressed:
    # if macropad.encoder_switch_debounced.released:

    if last_knob_pos is not macropad.encoder:  # knob has been turned
        knob_pos = macropad.encoder  # read encoder
        knob_delta = knob_pos - last_knob_pos  # compute knob_delta since last read
        last_knob_pos = knob_pos  # save new reading

        if knob_delta > 0:
            macropad.keyboard.send(Keycode.LEFT_SHIFT, Keycode.RIGHT_ARROW)
        elif knob_delta < 0:
            macropad.keyboard.send(Keycode.LEFT_SHIFT, Keycode.LEFT_ARROW)

        last_knob_pos = macropad.encoder
