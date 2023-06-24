#!/usr/bin/env python3
import grpc
from concurrent import futures
from PIL import Image
from scipy.signal import convolve2d
import numpy as np
import image_pb2
import image_pb2_grpc
import io

class NLImageServiceServicer(image_pb2_grpc.NLImageServiceServicer):
    def RotateImage(self, request, context):
        # Load the image from bytes
        try:
            image = Image.open(io.BytesIO(request.image.data))
        except:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid image data')
            print('Invalid image data')

        # Determine the rotation based on the enum value
        if request.rotation == image_pb2.NLImageRotateRequest.NINETY_DEG:
            image = image.rotate(-90)  # PIL rotates counter clockwise
        elif request.rotation == image_pb2.NLImageRotateRequest.ONE_EIGHTY_DEG:
            image = image.rotate(-180)
        elif request.rotation == image_pb2.NLImageRotateRequest.TWO_SEVENTY_DEG:
            image = image.rotate(-270)

        # Convert the image back to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        return image_pb2.NLImage(color=request.image.color, data=img_byte_arr, width=image.width, height=image.height)

    def MeanFilter(self, request, context):
        # Load the image from bytes
        try:
            image = Image.open(io.BytesIO(request.data))
        except:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Invalid image data')
            print('Invalid image data')

        # Convert the image to a numpy array for easier manipulation
        np_image = np.array(image)

        # Apply a mean filter (3x3 convolution as descriped in image.proto)
        if len(np.array(np_image).shape) == 2:
          np_image = convolve2d(np.array(np_image), np.ones((3,3)), boundary='fill', mode='same')
        else:
          np_image1 = convolve2d(np.array(np_image)[:,:,0], np.ones((3,3)), boundary='fill', mode='same')
          np_image2 = convolve2d(np.array(np_image)[:,:,1], np.ones((3,3)), boundary='fill', mode='same')
          np_image3 = convolve2d(np.array(np_image)[:,:,2], np.ones((3,3)), boundary='fill', mode='same')
          np_image = np.dstack((np_image1, np_image2, np_image3))

        np_image[1:-1, [0,-1]] = np_image[1:-1, [0,-1]]/6
        np_image[[0,-1], 1:-1] = np_image[[0,-1], 1:-1]/6
        np_image[0,0] = np_image[0,0]/4
        np_image[-1,0] = np_image[-1,0]/4
        np_image[0,-1] = np_image[0,-1]/4
        np_image[-1,-1] = np_image[-1,-1]/4
        np_image[1:-1, 1:-1] = np_image[1:-1, 1:-1]/9
        np_image = np_image.astype(np.uint8)
        
        # Or can use cv2.blur which is a very good approximation of appove operations:
        # np_image = cv2.blur(np_image, (3,3), borderType=cv2.BORDER_DEFAULT)
        
        # Convert the numpy array back to an image
        image = Image.fromarray(np_image)

        # Convert the image back to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        return image_pb2.NLImage(color=request.color, data=img_byte_arr, width=image.width, height=image.height)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_NLImageServiceServicer_to_server(NLImageServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
