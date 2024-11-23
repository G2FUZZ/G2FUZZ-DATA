import numpy as np
from PIL import Image

# Create a more complex image with multiple patterns and color variations
image_data = np.zeros((200, 200, 3), dtype=np.uint8)
image_data[::20, ::20] = [255, 255, 255]  # Add a white pattern
image_data[50:150, 50:150] = [0, 255, 0]  # Add a green square
image_data[100:180, 10:90] = [0, 0, 255]  # Add a blue rectangle

# Save the image as a JPEG file with different quality settings to observe compression artifacts
for quality in range(1, 11):
    image = Image.fromarray(image_data)
    image.save(f'./tmp/complex_compression_artifacts_q{quality}.jpg', quality=quality * 10)