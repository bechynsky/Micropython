import dht
import machine

# Wemos D1 Mini DHT Shield is on pin 2 (D4)
d = dht.DHT22(machine.Pin(2))
d.measure()

print(d.temperature())
print(d.humidity())
