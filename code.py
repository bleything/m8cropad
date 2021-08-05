from adafruit_macropad import MacroPad

from constants import *

################################################################################
### config
################################################################################

### which way do you want the knob to point? UP, DOWN, LEFT, or RIGHT

KNOB_GOES = "UP"

### set the colors for the various buttons and states. See COLOR_CODES in
### constants.py for the list of color names

COLORS = {
    "pressed":  COLOR_CODES["orange"],
    "arrows":   COLOR_CODES["cyan"],
    "function": COLOR_CODES["purple"],
    "shift":    COLOR_CODES["pink"],
    "play":     COLOR_CODES["green"]
}

################################################################################
### shouldn't need to edit anything below here
################################################################################

angle = ORIENTATIONS[KNOB_GOES]["angle"]
orientation = ORIENTATIONS[KNOB_GOES]["orientation"]
macropad = MacroPad(rotation=angle)  # create the macropad object, rotate orientation

################################################################################
### key and LED setup
################################################################################

macropad.pixels.brightness = 0.1
macropad.pixels.fill(0)

keys = {}

for key, config in KEY_CONFIG.items():
    key_number = config["key"][orientation]
    color = COLORS[config["color"]]

    keys[key_number] = config
    keys[key_number]["color"] = color

    macropad.pixels[key_number] = color

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
                keycode = keys[key]["code"]

                macropad.pixels[key] = COLORS["pressed"]
                macropad.keyboard.press(keycode)
            except KeyError:
                # undefined key; move along
                pass

        if key_event.released:
            key = key_event.key_number
            text_lines[1].text = "release: {}".format(key)

            try:
                keycode = keys[key]["code"]
                color = keys[key]["color"]

                macropad.pixels[key] = color
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
