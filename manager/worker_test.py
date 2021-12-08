import socket

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
# print("Please input:")
# out_data = input()
while True:
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    print("Please input:")
    out_data = input()
    client.send(out_data.encode("utf-8"))
    if out_data == 'bye':
        break
client.close()
