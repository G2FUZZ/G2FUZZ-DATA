import numpy as np
import cv2

# Create a 1-bit monochrome BMP image
monochrome_image = np.array([[0, 1, 0],
                              [1, 0, 1],
                              [0, 1, 0]], dtype=np.uint8) * 255
cv2.imwrite('./tmp/monochrome.bmp', monochrome_image)

# Create an 8-bit grayscale BMP image
grayscale_image = np.array([[100, 150, 200],
                            [50, 75, 25],
                            [225, 125, 175]], dtype=np.uint8)
cv2.imwrite('./tmp/grayscale.bmp', grayscale_image)

# Create a 24-bit true color BMP image
true_color_image = np.zeros((3, 3, 3), dtype=np.uint8)
true_color_image[:, :, 0] = np.array([[255, 0, 0],
                                      [0, 255, 0],
                                      [0, 0, 255]])
true_color_image[:, :, 1] = np.array([[0, 255, 255],
                                      [255, 0, 255],
                                      [255, 255, 0]])
true_color_image[:, :, 2] = np.array([[255, 255, 0],
                                      [255, 0, 255],
                                      [0, 255, 255]])
cv2.imwrite('./tmp/true_color.bmp', true_color_image)