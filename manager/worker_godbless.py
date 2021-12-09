# !pip install torch
import socket
import sys
import random
import torchvision
import torch
import numpy as np
import json


# load labels and GoogleNet
def initialize_model():
    print(">>> Initialize the model...")
    # load labels
    with open('./imagenet_label.json', 'r', encoding='utf8') as fp:
        the_imagenet_label = json.load(fp)

    # import model
    print(">>> Loading GoogleNet..")
    the_model = torchvision.models.googlenet(pretrained=True)
    the_model.eval()
    print(">>> Finished.")

    return the_model, the_imagenet_label


# Get full image message from manager
def get_full_message(manager_socket):
    msg = ""
    while True:
        # Get the full message
        unit_msg = manager_socket.recv(buffer_size)
        if len(unit_msg) == 0:
            manager_socket.close()
            print(">>> Disconnected with manager")
            break
        msg += unit_msg.decode("utf-8")
        if msg[-1] == '\n':
            break
    return msg


# The image message decoder
def decoder(image_message):
    print(image_message)
    decoded_msg = image_message.split(" ", 3)
    """
    decoded_msg[0] - seqnum
    decoded_msg[1] - row(pixel)
    decoded_msg[2] - column(pixel)
    decoded_msg[3] - image data
    """
    print(">>> Received a image, seqnum = " + decoded_msg[0])
    the_seqnum = int(decoded_msg[0])
    row_size = int(decoded_msg[1])
    column_size = int(decoded_msg[2])
    the_image = decoded_msg[3].split()
    # decode image and translate it to tensor
    the_image = np.array(the_image).astype(np.float32).reshape(3, row_size, column_size)
    the_image = torch.from_numpy(the_image)

    return the_seqnum, the_image


# Image Recognition
def image_recognition(_image):
    imgs = [_image]
    imgs = torch.tensor([item.detach().numpy() for item in imgs])
    print(">>> Start prediction..")
    predictions = model(imgs)
    pred_numpy = predictions[0].detach().numpy()
    pred_index = np.argmax(pred_numpy)
    pred_class = imagenet_label[str(pred_index)]
    print('>>> Prediction finished. class: ' + pred_class)

    return pred_class


# accept command line arguments
argv = sys.argv[1:]
# create socket object
worker_socket = socket.socket()
# the probability of node failure
fail_pr = None
# the seqnum of the last received image
last_seqnum = 0
# the classification of the last received image
last_result = "apple"
# training parameters
model = None
imagenet_label = None

buffer_size = 1024

# initialize model
model, imagenet_label = initialize_model()


try:
    worker_socket = socket.create_connection(('DESKTOP-3N4U79Q', 2888))
    print(">>> Connected with manager")
    image_msg = ""
    while True:
        print(">>> Wait for image message from manager...")
        image_msg = get_full_message(worker_socket)
        seqnum, image = decoder(image_msg)

        # Check if the new received image is duplicate
        if seqnum != last_seqnum:
            last_result = image_recognition(image)
            last_seqnum = seqnum

        print(">>> Send the image recognition result back\n")
        result_msg = str(last_seqnum) + " " + last_result + "\n"
        worker_socket.send(result_msg.encode("utf-8"))
except Exception as e:
    print(e)

print(">>> Stop worker")
worker_socket.close()
