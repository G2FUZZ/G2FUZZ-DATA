import numpy as np
from PIL import Image

# Generate a simple 100x100 image with random pixel values (representing colors)
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Add a color profile to the image (simulated as a random array)
color_profile = np.random.randint(0, 256, (100,), dtype=np.uint8)
image.info['color_profile'] = color_profile.tobytes()

# Save the image with the embedded color profile
image.save('./tmp/embedded_image.jpg')

print("Image with embedded color profile saved successfully.")