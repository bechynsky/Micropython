import dht
import machine
import neopixel
import time

def main():
    # Wemos D1 Mini NeoPixel Shield is on pin 4 (D2)
    pin = machine.Pin(4, machine.Pin.OUT)
    n = neopixel.NeoPixel(pin, 1)
    # Wemos D1 Mini DHT Shield is on pin 2 (D4)
    d = dht.DHT22(machine.Pin(2))

    while True:
        d.measure()
        h = d.humidity()
        print(h)

        if (h < 45):
            n[0] = (127, 0, 0)
        else:
            n[0] = (0, 127, 0)
        n.write()

        time.sleep(10)

main()