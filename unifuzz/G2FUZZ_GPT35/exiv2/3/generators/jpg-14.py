import numpy as np
from PIL import Image

# Create a random RGB image
width = 100
height = 100
image_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(image_data, 'RGB')

# Create a thumbnail image
thumbnail_size = (50, 50)
thumbnail = image.resize(thumbnail_size)

# Add thumbnail to the image metadata
image.thumbnail(thumbnail_size)
image.paste(thumbnail)

# Define compression levels
compression_levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Save the image with different compression levels
for level in compression_levels:
    image.save(f'./tmp/generated_image_compression_{level}_with_thumbnail.jpg', quality=level)