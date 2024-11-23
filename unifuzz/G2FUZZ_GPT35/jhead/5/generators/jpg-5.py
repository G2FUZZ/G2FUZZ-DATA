import numpy as np
from PIL import Image

# Create a white image of size 100x100 pixels
image = np.ones((100, 100, 3), dtype=np.uint8) * 255
image = Image.fromarray(image)

# Save the image as a jpg file
image.save("./tmp/compatibility.jpg")

print("Compatibility jpg file generated successfully!")