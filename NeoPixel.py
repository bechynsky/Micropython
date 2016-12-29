from machine import Pin
from neopixel import NeoPixel

# Wemos D1 Mini NeoPixel Shield is on pin 4 (D2)
pin = Pin(4, Pin.OUT)
n = NeoPixel(pin, 1)
n[0] = (255, 0, 0)
n.write()
