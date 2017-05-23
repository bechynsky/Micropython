import machine
import neopixel
import time

# LED count
ledsCount = 8
# Wemos D1 Mini NeoPixel Shield is on pin 4 (D2)
pin = machine.Pin(4, machine.Pin.OUT)
# There is just 1 Neopixel LED on Shield
n = neopixel.NeoPixel(pin, ledsCount)
while True:
    # RGB values
    for led in range(ledsCount):
        n[led] = (200, 0, 0)
    # Write value to LEDs
    n.write()
    time.sleep(2)

    for led in range(ledsCount):
        n[led] = (0, 200, 0)
    n.write()
    time.sleep(2)

    for led in range(ledsCount):
        n[led] = (0, 0, 200)
    n.write()
    time.sleep(2)