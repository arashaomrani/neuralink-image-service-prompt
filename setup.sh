#!/bin/bash
sudo apt-get update
sudo apt-get install -y python3.8 python3-pip
pip3 install grpcio grpcio-tools protobuf pillow numpy scipy opencv-python
