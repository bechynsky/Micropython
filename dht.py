# DHT11 and DHT22 library
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/dht.html
import dht
# functions related to the board - http://docs.micropython.org/en/latest/esp8266/library/machine.html
import machine

# Wemos D1 Mini DHT Shield is on pin 2 (D4)
# Use ESP8266 GPIO pin numbers
# https://www.wemos.cc/product/d1-mini-pro.html
d = dht.DHT22(machine.Pin(2))
# Ask for data
d.measure()

print(d.temperature())
print(d.humidity())
