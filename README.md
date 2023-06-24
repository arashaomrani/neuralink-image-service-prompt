# neuralink-image-service-prompt
This project is an implementation of an image rotation and mean filter service using gRPC. The service can rotate an image by 90, 180, or 270 degrees, and apply a mean filter to an image. The client can specify the image to be processed, the operations to be performed, and the location of the output image. Both color and grayscale images are supported.

## Project Structure

- `proto/image.proto`: The Protocol Buffers definition file for the image service.
- `build.sh`: Run this file in the Linux environment to create `image_pb2.py` and `image_pb2_grpc.py` from `proto/image.proto`.
- `setup.sh`: Run this file in the Linux environment to update the system, install python3 and pip3 and also install required python libararies.
- `server.py`: The Python script for the image service server.
- `client.py`: The Python script for the image service client.

## Run Server:
### Run server locally:
to run server locally can use following command:
python3 server.py --host localhost --port 50051
