import numpy as np
from PIL import Image

# Create a transparent image with alpha channel
width = 100
height = 100
transparent_color = (0, 0, 0, 0)  # RGBA (0,0,0,0) represents transparent black
image = Image.new("RGBA", (width, height), transparent_color)

# Save the image to a BMP file
image.save("./tmp/transparent_image.bmp")