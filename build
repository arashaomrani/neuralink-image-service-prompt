#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Define the directory where the Python files will be generated.
OUT_DIR="./"

# Generate the Python files.
python3 -m grpc_tools.protoc -I./proto --python_out=$OUT_DIR --grpc_python_out=$OUT_DIR ./proto/image.proto

mv client.py client
mv server.py server
