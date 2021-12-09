"""
This is the client file for part1.
You can input texts to send to the server and then the server
will echo the message back.


author: Yuhang Sun
assignment: PA1
"""
# !pip install torch
import socket
from threading import Thread
from PIL import Image
import torchvision.transforms as transforms

g_socket = None
g_conn_pool = []
g_conn_use = []


def get_image():
    img = Image.open('images/dog.jpeg').convert('RGB')
    img = transforms.ToTensor()(img)
    row = img.shape[1]
    column = img.shape[2]
    ss = "1 " + str(row) + " " + str(column) + " "
    img_numpy = img.numpy().flatten()
    for num in img_numpy:
        ss += str(num) + ' '

    return ss


def handle_client():
    while True:
        client, addr = g_socket.accept()
        print(addr)
        g_conn_pool.append(client)
        g_conn_use.append(False)


def handle_send_image(client, ind):
    msg = get_image()
    print(">>> Sending the image..")
    msg += "\n"
    client.send(msg.encode("utf-8"))
    print(">>> Finish sending.")
    # receive the feedback from the server
    msg = ""
    while True:
        feedback = client.recv(1024)
        if msg == "404":
            raise Exception
        msg += feedback.decode("utf-8")
        if msg[-1] == '\n':
            break
    print(">>> Receive from the client: " + msg)
    g_conn_use[ind] = False


def main():
    global g_socket, g_conn_pool
    g_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g_socket.bind(('DESKTOP-3N4U79Q', 2888))
    g_socket.listen(5)
    print("服务端已启动，等待客户端连接...")

    t = Thread(target=handle_client)
    t.setDaemon(True)
    t.start()
    while True:
        cmd = input("请输入操作：")
        if cmd == '':
            continue
        if int(cmd) == 1:
            print("当前已连接worker：", len(g_conn_pool))
            for i in range(len(g_conn_pool)):
                if not g_conn_use[i]:
                    print(">>> Use worker " + str(i + 1))
                    g_conn_use[i] = True
                    t = Thread(target=handle_send_image, args=(g_conn_pool[i], i))
                    t.setDaemon(True)
                    t.start()
                    break
        if cmd == 'exit':
            exit()


if __name__ == '__main__':
    main()
