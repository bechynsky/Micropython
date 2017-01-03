# TCP support
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html
import socket

# Address info from DHCP
addr = socket.getaddrinfo('micropython.org',80)[0][-1]

# Connect to address and port using TCP
s = socket.socket()
s.connect(addr)

# Send HTTP protocol request
# We work with HTTP protocol directly using GET method
# https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
# Read first 1 kB of data
data = s.recv(1024)
# Close connection
s.close()

print(data)
