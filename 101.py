import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)

while True:
    pin.value(1);
    time.sleep(0.5)
    pin.value(0);
    time.sleep(0.5)