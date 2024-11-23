import numpy as np
from PIL import Image

# Define image size
width = 100
height = 100

# Create a white image
image_white = Image.new("RGB", (width, height), "white")
image_white.save("./tmp/bmp_bottom_up.bmp")

# Create a black image
image_black = Image.new("RGB", (width, height), "black")
image_black.save("./tmp/bmp_top_down.bmp")