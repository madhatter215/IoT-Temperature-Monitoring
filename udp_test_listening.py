#!/usr/bin/python
import socket
import os

UDP_IP = "147.11.46.69"
UDP_PORT = 5005
PATH=r"/var/tmp/temperature_sensor2.dat"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

#Initialize file
my_file = open(PATH, 'w')
#my_file.write("\
#yyyy-mm-dd hh:mm:ss degrees F\n")
my_file.close()


def split_message(msg):
    array = msg.split(" ")
    #print array
    return array[0] + " " + array[1] + " " + array[5]

def append_to_file(msg):
    my_file = open(PATH, 'a')
    my_file.write(split_message(msg) + "\n")
    my_file.close()


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    append_to_file(data)



