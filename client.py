#!/usr/bin/env python3
import grpc
import image_pb2
import image_pb2_grpc
import argparse
import io

def run():
    parser = argparse.ArgumentParser(description='Image processing client.')
    parser.add_argument('--input', type=str, help='Path to the input image.')
    parser.add_argument('--output', type=str, help='Path to save the output image.')
    parser.add_argument('--rotate', type=str, choices=['NONE', 'NINETY_DEG', 'ONE_EIGHTY_DEG', 'TWO_SEVENTY_DEG'], default='NONE', help='Rotation to apply to the image.')
    parser.add_argument('--mean', action='store_true', help='Apply mean filter to the image.')
    parser.add_argument('--port', type=str, default='50051', help='Port of the server.')
    parser.add_argument('--host', type=str, default='localhost', help='Host of the server.')

    args = parser.parse_args()

    with open(args.input, 'rb') as f:
        image_data = f.read()

    channel = grpc.insecure_channel(f'{args.host}:{args.port}')
    stub = image_pb2_grpc.NLImageServiceStub(channel)

    if args.rotate != 'NONE':
        rotation = image_pb2.NLImageRotateRequest.Rotation.Value(args.rotate)
        image = image_pb2.NLImage(color=True, data=image_data, width=0, height=0)  # assuming color image and size not known
        request = image_pb2.NLImageRotateRequest(rotation=rotation, image=image)
        response = stub.RotateImage(request)
        image_data = response.data

    if args.mean:
        image = image_pb2.NLImage(color=True, data=image_data, width=0, height=0)  # assuming color image and size not known
        response = stub.MeanFilter(image)
        image_data = response.data

    with open(args.output, 'wb') as f:
        f.write(image_data)

if __name__ == '__main__':
    run()
