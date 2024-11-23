import numpy as np
import cv2

# Create a 32-bit floating-point BMP image with 4 channels (RGBA)
rgba_image = np.zeros((3, 3, 4), dtype=np.float32)
rgba_image[:, :, 0] = np.array([[1.0, 0.0, 0.0],
                                [0.0, 1.0, 0.0],
                                [0.0, 0.0, 1.0]])
rgba_image[:, :, 1] = np.array([[0.0, 1.0, 1.0],
                                [1.0, 0.0, 1.0],
                                [1.0, 1.0, 0.0]])
rgba_image[:, :, 2] = np.array([[1.0, 1.0, 0.0],
                                [1.0, 0.0, 1.0],
                                [0.0, 1.0, 1.0]])
rgba_image[:, :, 3] = np.array([[0.5, 0.5, 0.5],
                                [0.5, 0.5, 0.5],
                                [0.5, 0.5, 0.5]]) * 255
cv2.imwrite('./tmp/rgba_image.bmp', np.uint8(rgba_image * 255))

# Create a 16-bit grayscale BMP image
grayscale_16bit_image = np.array([[2000, 4000, 6000],
                                 [8000, 10000, 12000],
                                 [14000, 16000, 18000]], dtype=np.uint16)
cv2.imwrite('./tmp/grayscale_16bit.bmp', grayscale_16bit_image)