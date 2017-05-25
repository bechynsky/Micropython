# Do not use this code in real projects! Read
# http_server_simplistic_commented.py for details.
import socket

import machine
import dht


CONTENT = b"""\
HTTP/1.0 200 OK

<h1>Micropython weather station</h1>
<p>Temperature: {0} °C</p>
<p>Humidity: {1}%</p>
"""

# Wemos D1 Mini DHT Shield is on pin 2 (D4)
# Use ESP8266 GPIO pin numbers
# https://www.wemos.cc/product/d1-mini-pro.html
d = dht.DHT11(machine.Pin(2))

def main():
    s = socket.socket()
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(addr)
    s.listen(1)
    print("Listening, connect your browser to http://<this_host>/")

    counter = 0
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(128)

        print(req)

        d.measure()

        t = d.temperature()
        h = d.humidity()

        client_s.send(CONTENT.format(t, h))
        client_s.close()
        counter += 1
        print()


main()

