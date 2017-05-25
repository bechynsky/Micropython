# Do not use this code in real projects! Read
# http_server_simplistic_commented.py for details.
try:
    import usocket as socket
except:
    import socket

import machine


CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""
def getCommand(response):
    response = response.decode("utf-8")
    start = response.find(" ")
    end = response.find(" ", start+1)
    
    return(response[start+1:end])

def main():
    led = machine.Pin(2, machine.Pin.OUT)
    led.value(1)
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")

    counter = 0
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(1024)
        cmd = getCommand(req)
        
        print(cmd)

        if (cmd == "/on"):
            led.value(0)
        elif (cmd == "/off"):
            led.value(1)
        
        client_s.send(CONTENT % counter)
        client_s.close()
        counter += 1
        print()


main()

