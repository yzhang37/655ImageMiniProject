from threading import Thread
import socket

g_socket = None
g_conn_pool = []
g_conn_use = []


def client_thread(client_socket, i):
    client_socket.send(("request " + str(i) + " from manager").encode("utf-8"))
    # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
    while True:
        data = client_socket.recv(1024)
        msg = data.decode()
        if msg == 'bye':
            break
        print("from client", msg)
    print("Client at ", clientAddress, " disconnected...")


def main():
    global g_socket, g_conn_pool
    g_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g_socket.bind(('127.0.0.1', 8080))
    g_socket.listen(5)
    print("Server started")
    print("Waiting for client request..")
    g_socket.listen(5)
    for i in range(2):
        client, addr = g_socket.accept()
        print(addr)
        g_conn_pool.append(client)
        g_conn_use.append(False)

    while True:
        cmd = input("qing: ")
        for i in range(len(g_conn_pool)):
            t = Thread(target=client_thread, args=(g_conn_pool[i], i + 1))
            t.start()


if __name__ == "__main__":
    main()
