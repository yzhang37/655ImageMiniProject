"""
This is the client file for part1.
You can input texts to send to the server and then the server
will echo the message back.
author: Yuhang Sun
assignment: PA1
"""
# !pip install torch
import socket
import sys
import numpy as np
from PIL import Image
import torchvision.transforms as transforms


def get_image():
    img = Image.open('images/dog.jpeg').convert('RGB')
    img = transforms.ToTensor()(img)
    ss = "1 750 750 "
    img_numpy = img.numpy().flatten()
    for num in img_numpy:
        ss += str(num) + ' '

    return ss
# # accept command line arguments


argv = sys.argv[1:]

tcpClientSocket = socket.socket()
# get host name and port number
if len(argv) == 0:
    host = input("Please enter server's hostname:\n")
    port = int(input("Please enter the port number of server:\n"))
else:
    host = argv[0]
    port = int(argv[1])

buffer_size = 1024

# connect to server
try:
    tcpClientSocket.connect((host, port))

# if connect failed, throw the exception
except Exception as e:
    print(e)
    sys.exit()

print("Server address: " + host + ": " + str(port))
# send a message
try:
    while True:
        msg = input("Please enter what you want to send: ")
        if msg == '1':
            msg = get_image()
        print(">>> Sending the image..")
        msg += "\n"
        tcpClientSocket.send(msg.encode("utf-8"))
        print(">>> Finish sending.")

        # receive the feedback from the server
        msg = ""
        while True:
            feedback = tcpClientSocket.recv(buffer_size)
            if msg == "404":
                raise Exception
            msg += feedback.decode("utf-8")
            if msg[-1] == '\n':
                break
        print(">>> Receive from the server: " + msg)
except Exception as e:
    print("detected disconnection")

tcpClientSocket.close()