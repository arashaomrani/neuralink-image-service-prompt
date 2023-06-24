# neuralink-image-service-prompt
This project is an implementation of an image rotation and mean filter service using gRPC. The service can rotate an image by 90, 180, or 270 degrees, and apply a mean filter to an image. The client can specify the image to be processed, the operations to be performed, and the location of the output image. Both color and grayscale images are supported.

## Project Structure

- This solution requires cleen installation of Ubuntu 22.04.
- `proto/image.proto`: The Protocol Buffers definition file for the image service.
- `build.sh`: Run this file in the Ubuntu environment to create `image_pb2.py` and `image_pb2_grpc.py` from `proto/image.proto`.
- `setup.sh`: Run this file in the Ubuntu environment to update the system, install python3 and pip3 and also install required python libararies.
- `server.py`: The Python script for the image service server.
- `client.py`: The Python script for the image service client.

## Run Server:
### Run server locally:
To run server locally, can use following command: `python3 server.py --host localhost --port 50051`
### Run server remotely: 
To run server to be accessible from a remote machine, can use following command: `python3 server.py --host 0.0.0.0 --port 50051` 
The --host argument of the server script should be set to 0.0.0.0 to accept connections from any IP address.

## Run Client:
To run client, run the following command: `python3 client.py --input path_to_input.png --output path_to_output.png --rotate NINETY_DEG --mean --host server_public_ip_or_hostname --port 50051`

Client can accept 3 inputs (`NINETY_DEG`, `ONE_EIGHTY_DEG`, `TWO_SEVENTY_DEG`) for 90, 180, 270 degree rotations.

