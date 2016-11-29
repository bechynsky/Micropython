import usocket as _socket
import ussl as ssl
import dht
import machine

SAS = ""
HOST = ""
DEVICE = ""

DHT_PIN = 2

def main(use_stream=True):
    d = dht.DHT22(machine.Pin(DHT_PIN))
    d.measure()

    s = _socket.socket()

    ai = _socket.getaddrinfo(HOST, 443)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    data = b"{'t': " + str(d.temperature()) + ", 'h': " + str(d.humidity()) + "}"

    s.write("POST /devices/" + DEVICE + "/messages/events?api-version=2016-02-03 HTTP/1.0\r\n")
    s.write("Host: " + HOST + "\r\n")
    s.write("Authorization: " + SAS + "\r\n")
    s.write("Content-Type: application/json\r\n")
    s.write("Connection: close\r\n")
    s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
    s.write(data)
    print(s.read(128))

    s.close()


main()