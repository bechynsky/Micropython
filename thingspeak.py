import usocket as _socket
import ussl as ssl
import dht
import machine
import time

API_KEY = ""
DHT_PIN = 2
HOST = "api.thingspeak.com"

d = dht.DHT11(machine.Pin(DHT_PIN))

def main(use_stream=True):
    while True:
        d.measure()
        data = b"api_key="+ API_KEY + "&field1=" + str(d.temperature()) + "&field2=" + str(d.humidity())
      
        s = _socket.socket()
        ai = _socket.getaddrinfo(HOST, 443)
        addr = ai[0][-1]
        s.connect(addr)
    
        s = ssl.wrap_socket(s)
    
        
        s.write("POST /update HTTP/1.0\r\n")
        s.write("Host: " + HOST + "\r\n")
        s.write("Content-Length: " + str(len(data)) + "\r\n\r\n")
        s.write(data)
        print(s.read(128))
    
        s.close()
        time.sleep(60)
        
main()
