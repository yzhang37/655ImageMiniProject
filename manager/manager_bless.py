# !pip install torch
# python manager.py <total_image_num>
import socket
import sys
import time
from threading import Thread
from threading import Event
from multiprocessing import Queue, Process, Value, Array, Manager
from PIL import Image
import torchvision.transforms as transforms


def check_if_work():
    global images, idle_workers
    if (not images.empty()) and (not idle_workers.empty()):
        return True
    else:
        return False


def get_image(image_id):
    img = Image.open('temp/' + image_id).convert('RGB')
    img = transforms.ToTensor()(img)
    row = img.shape[1]
    column = img.shape[2]
    ss = image_id + " " + str(row) + " " + str(column) + " "
    img_numpy = img.numpy().flatten()
    for num in img_numpy:
        ss += str(num) + ' '
    return ss


def collect_image_result(msg):
    decoded_result = msg.split(" ", 1)
    msg_id = decoded_result[0]
    result = decoded_result[1].split("\n")[0]
    return msg_id, result


def output_statistics():
    global total_img_size, total_time
    print("---------------- statistics -------------------")
    print(results)
    print("Total Image Size: " + str(total_img_size) + "bits")
    print("Total Time: " + str(total_time) + "seconds")
    throughput = total_img_size / total_time
    print("Throughput: " + str(throughput) + "bps")


def snd_rcv_img(worker, _id):
    global start_time, img_num_count, images, conn_pool, \
        workers_limit, idle_workers, last_img_id, results, \
        total_img_size, total_img_num, total_time

    try:
        if img_num_count == 0:
            start_time = time.time()
        img_id = images.get()
        img_msg = get_image(img_id) + "\n"
        worker.send(img_msg.encode("utf-8"))
        print(">>> Send one image to worker" + str(_id + 1))
        print(time.time())
        while True:
            msg = ""
            while True:
                feedback = worker.recv(buffer_size)
                msg += feedback.decode("utf-8")
                if msg[-1] == '\n':
                    break
            if msg == "404\n":
                print(">>> Detected disconnection with Worker" + str(_id + 1))
                images.put(img_id)
                raise Exception
            print(">>> Receive from the server: " + msg)
            print(time.time())
            this_img_id, this_result = collect_image_result(msg)
            if this_img_id == last_img_id[_id]:
                worker.send(img_msg.encode("utf-8"))
                continue
            else:
                last_img_id[_id] = this_img_id
                results[this_img_id] = this_result
                total_img_size += len(img_msg.encode("utf-8")) * 8
                img_num_count += 1
                if img_num_count == total_img_num:
                    total_time = time.time() - start_time
                    output_statistics()
                    img_num_count = 0
                break
        idle_workers.put(_id)
    except Exception as e:
        print(e)
        # Handle if one worker failed
        conn_pool[_id].close()
        if workers_limit < 6:
            idle_workers.put(workers_limit - 1)
            print(">>> Start assigning works to Worker" + str(workers_limit))
            workers_limit += 1
        else:
            print(">>> There is no available worker anymore.")


# Timer Class
# class RepeatTimer(Thread):
#     def __init__(self, event, client_socket, thread_id, image_msg):
#         Thread.__init__(self)
#         self.stopped = event
#         self.client_socket = client_socket
#         self.thread_id = thread_id
#         self.image_msg = image_msg
#
#     def run(self) -> None:
#         while not self.stopped.wait(1000):
#             send_image(self.client_socket, self.image_msg)
#             print(">>> Timeout! Send the image again to worker" + str(self.thread_id))


argv = sys.argv[1:]
total_img_num = int(argv[0])
required_workers_num = 2  # set 1-5
workers_limit = Value('i', required_workers_num + 1)
conn_pool = []
images = Queue(maxsize=20)
idle_workers = Queue(maxsize=5)
buffer_size = 1024
img_num_count = 0
total_img_size = 0  # bit
start_time = 0.0
total_time = 0.0  # second
last_img_id = {
    0: "",
    1: "",
    2: "",
    3: "",
    4: ""
}
results = {"": ""}


def main():
    # global conn_pool, idle_workers, required_workers_num, images

    images.put("warrior.jpeg")
    images.put("dog.jpeg")
    images.put("bu.jpeg")

    # Build connection with workers
    manager_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    manager_socket.bind(("localhost", 2888))
    manager_socket.listen(5)
    print(">>> Manager starts. Connecting to workers...")
    for i in range(2):  # set range(5)
        worker, addr = manager_socket.accept()
        conn_pool.append(worker)
        if i < required_workers_num:
            idle_workers.put(i)
    print(">>> Connected with all 5 nodes")

    while True:
        while check_if_work():
            worker_id = idle_workers.get()
            print(worker_id)
            print(time.time())
            worker_thread = Process(target=snd_rcv_img, args=(conn_pool[worker_id], worker_id))
            worker_thread.start()


if __name__ == '__main__':
    main()
