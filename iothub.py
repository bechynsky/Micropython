# TCP support
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html
import socket
# SSL wrapper for Socket
import ussl
# DHT11 and DHT22 library
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/dht.html
import dht
# functions related to the board - http://docs.micropython.org/en/latest/esp8266/library/machine.html
import machine

# Azure IoT Hub configuration
# https://docs.microsoft.com/en-us/azure/iot-hub/
# Shared Access Signature
SAS = ""
# Host name
HOST = ""
# Device name
DEVICE = ""

# Wemos D1 Mini DHT Shield is on pin 2 (D4)
# Use ESP8266 GPIO pin numbers
# https://www.wemos.cc/product/d1-mini-pro.html
d = dht.DHT22(machine.Pin(2))

def main(use_stream=True):
    # Ask for data
    d.measure()
    data = b"{'t': " + str(d.temperature()) + ", 'h': " + str(d.humidity()) + "}"

    s = socket.socket()

    ai = socket.getaddrinfo(HOST, 443)
    addr = ai[0][-1]
    s.connect(addr)

    # SSL wrap
    s = ussl.wrap_socket(s)
    
    # Send POST request to Azure IoT Hub
    s.write("POST /devices/" + DEVICE + "/messages/events?api-version=2016-02-03 HTTP/1.0\r\n")
    # HTTP Headers
    s.write("Host: " + HOST + "\r\n")
    s.write("Authorization: " + SAS + "\r\n")
    s.write("Content-Type: application/json\r\n")
    s.write("Connection: close\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    # Data
    s.write(data)
    
    # Print 128 bytes of response
    print(s.read(128))

    s.close()

# Run
main()