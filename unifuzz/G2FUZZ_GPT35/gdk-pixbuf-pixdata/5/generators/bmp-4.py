import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Generate a 1-bit monochrome image
monochrome_image = np.random.randint(0, 2, size=(100, 100), dtype=np.uint8) * 255
Image.fromarray(monochrome_image).save('./tmp/monochrome.bmp')

# Generate an 8-bit grayscale image
grayscale_image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
Image.fromarray(grayscale_image, mode='L').save('./tmp/grayscale.bmp')

# Generate a 24-bit true color image
true_color_image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
Image.fromarray(true_color_image).save('./tmp/true_color.bmp')