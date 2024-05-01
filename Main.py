import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

while True:
    kbd.send(Keycode.KEYPAD_EIGHT)
    time.sleep(0.09)
