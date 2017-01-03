# DHT11 and DHT22 library
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/dht.html
import dht
# functions related to the board - http://docs.micropython.org/en/latest/esp8266/library/machine.html
import machine
# NeoPixels library https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html
import neopixel
import time

def main():
    # Wemos D1 Mini NeoPixel Shield is on pin 4 (D2)
    pin = machine.Pin(4, machine.Pin.OUT)
    # There is just 1 Neopixel LED on Shield
    n = neopixel.NeoPixel(pin, 1)
    # Wemos D1 Mini DHT Shield is on pin 2 (D4)
    d = dht.DHT22(machine.Pin(2))

    while True:
        d.measure()
        h = d.humidity()
        print(h)

        if (h < 45):
            # RGB values
            n[0] = (127, 0, 0)
        else:
            n[0] = (0, 127, 0)
        
        # Write value to LEDs
        n.write()

        time.sleep(10)

main()