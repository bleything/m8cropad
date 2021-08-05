m8cropad
================================================================================

This repo contains firmware that allows you to use the [Adafruit Macropad] as a
controller for the [M8 Tracker Headless]. To use, copy `code.py` and
`constants.py` to your macropad and then load up the [M8 Web Display].

[Adafruit Macropad]: https://www.adafruit.com/product/5128
[M8 Tracker Headless]: https://github.com/Dirtywave/M8HeadlessFirmware
[M8 Web Display]: https://derkyjadex.github.io/M8WebDisplay/

Requirements
--------------------------------------------------------------------------------

You'll need [CircuitPython]. I'm on 7.0.0-alpha.5 as of this writing. You'll
also need the libraries that shipped on the Macropad. On mine that was:

  * adafruit_debouncer.mpy
  * adafruit_display_text
  * adafruit_hid
  * adafruit_macropad.mpy
  * adafruit_midi
  * adafruit_pixelbuf.mpy
  * adafruit_simple_text_display.mpy
  * adafruit_simplemath.mpy
  * neopixel.mpy

[CircuitPython]: https://circuitpython.org/board/adafruit_macropad_rp2040/

Acknowledgements
--------------------------------------------------------------------------------

Thank you to Kattni Rembor and John Park at Adafruit for the libraries and
example code upon which this is based.

Special thanks to Matt Williams for the idea and inspiration.

License
--------------------------------------------------------------------------------

Copyright 2021 Ben Bleything, released under the terms of the MIT license. See
[`LICENSE`](LICENSE) for details.
