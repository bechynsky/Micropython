# functions related to the board - http://docs.micropython.org/en/latest/esp8266/library/machine.html
import machine
import time

# Define pin 2 as output
# There id build-in LED on pin 2, use ESP8266 GPIO pin numbers
# https://www.wemos.cc/product/d1-mini-pro.html
pin = machine.Pin(2, machine.Pin.OUT)

while True:
    # Set high voltage on pin
    pin.value(1);
    time.sleep(0.5)
    # Set low voltage on pin
    pin.value(0);
    time.sleep(0.5)