import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Convert the image to YCbCr color model
image_ycbcr = image.convert('YCbCr')

# Save the image in YCbCr color model with JPEG format (lossy compression)
image_ycbcr.save('./tmp/compressed_image_ycbcr.jpg')

print("JPEG file with YCbCr color model feature generated and saved successfully.")