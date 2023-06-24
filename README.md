# neuralink-image-service-prompt
This project is an implementation of an image rotation and mean filter service using gRPC. The service can rotate an image by 90, 180, or 270 degrees, and apply a mean filter to an image. The client can specify the image to be processed, the operations to be performed, and the location of the output image. Both color and grayscale images are supported.

## Project Structure

- This solution requires clean installation of macOS.
- `proto/image.proto`: The Protocol Buffers definition file for the image service.
- `setup.sh`: Run this file in the macOS environment to update the system, install python3 and pip3 and also install required python libararies. 
- `build.sh`: Run this file in the macOS environment to create `image_pb2.py` and `image_pb2_grpc.py` from `proto/image.proto`. and also to convert server.py and client.py to executable server and client.
- `server.py`: The Python script for the image service server.
- `client.py`: The Python script for the image service client.

## Run Server:
### Run server locally:
To run server locally, can use following command: `./server --host localhost --port 50051`
### Run server remotely: 
To run server to be accessible from a remote machine, can use following command: `./server --host 0.0.0.0 --port 50051` 
The --host argument of the server script should be set to 0.0.0.0 to accept connections from any IP address.

## Run Client:
To run client, run the following command: `./client --input path_to_input.png --output path_to_output.png --rotate NINETY_DEG --mean --host server_public_ip_or_hostname --port 50051`
Client can accept 3 inputs (`NINETY_DEG`, `ONE_EIGHTY_DEG`, `TWO_SEVENTY_DEG`) for 90, 180, 270 degree rotations.

## Discussion:
The limitations of this solution include:
- The server is not secured. It uses an insecure gRPC channel. In a production setting, you would want to use a secure channel with SSL/TLS.
- No unit tests or integration tests are provided. In a production setting, you would want to have comprehensive tests to ensure the system works as expected.

This problem was an interesting exercise in designing a simple gRPC service and client. gRPC is a powerful tool for building efficient, scalable, and distributed systems. The protobuf interface definition language provides a strong contract for communication between different parts of a system or even different systems, which is a great benefit for maintaining and evolving complex systems.

