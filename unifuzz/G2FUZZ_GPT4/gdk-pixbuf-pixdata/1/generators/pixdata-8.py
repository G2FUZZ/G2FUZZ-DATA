import numpy as np
from PIL import Image

# Define the palette: Each entry in the palette is an RGB triplet
palette = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0), # Yellow
]

# Create an image with indexed colors
# Size of the image (width, height)
image_size = (100, 100)
# Create an array of indices referring to the palette
# For demonstration, creating a gradient of indices
indices = np.zeros(image_size, dtype=np.uint8)

# Fill the array with indices referring to different colors in the palette
# For simplicity, dividing the image into 4 vertical stripes
stripe_width = image_size[0] // len(palette)
for i, color in enumerate(palette):
    indices[:, i*stripe_width:(i+1)*stripe_width] = i

# Convert the indices to an image
image = Image.fromarray(indices, mode='P')

# Apply the palette
image.putpalette([val for color in palette for val in color])

# Save the image
output_path = './tmp/indexed_color_image.png'
image.save(output_path)