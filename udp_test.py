#!/usr/bin/python
import socket
import test_mraa
import time

UDP_IP = "147.11.46.69"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
#print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

while True:
        sock.sendto(test_mraa.get_temp(), (UDP_IP, UDP_PORT))
        time.sleep(60*20)

