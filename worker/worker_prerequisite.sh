#!/bin/bash
wget https://github.com/yzhang37/655ImageMiniProject/blob/main/worker/imagenet_label.json
wget https://github.com/yzhang37/655ImageMiniProject/blob/main/worker/worker.py
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install libjpeg-dev zlib1g-dev
pip3 --no-cache-dir install torch==1.10.0+cpu torchvision==0.11.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
