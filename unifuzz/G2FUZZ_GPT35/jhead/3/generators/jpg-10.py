import numpy as np
from PIL import Image

# Create a white image
img = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8) * 255)

# Save the image as a jpg file
img.save("./tmp/small_jpg_file.jpg")