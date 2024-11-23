import numpy as np
from PIL import Image

# Create a random image
image_data = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
image = Image.fromarray(image_data)

# Save the image with JPEG format (lossy compression)
image.save('./tmp/compressed_image.jpg')

print("JPEG file with lossy compression generated and saved successfully.")