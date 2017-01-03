import machine
import neopixel
import time

# Wemos D1 Mini NeoPixel Shield is on pin 4 (D2)
pin = machine.Pin(4, machine.Pin.OUT)
# There is just 1 Neopixel LED on Shield
n = neopixel.NeoPixel(pin, 1)
while True:
     # RGB values
    n[0] = (200, 0, 0)
    # Write value to LEDs
    n.write()
    time.sleep(2)
    n[0] = (0, 200, 0)
    n.write()
    time.sleep(2)
    n[0] = (0, 0, 200)
    n.write()
    time.sleep(2)