import os
from PIL import Image

# Create a new directory to store the generated ICO files
os.makedirs('./tmp/', exist_ok=True)

# Define the image sizes for different resolutions
image_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]

# Extract the maximum width and height from the image sizes
max_width = max(size[0] for size in image_sizes)
max_height = max(size[1] for size in image_sizes)

# Create an empty image to store all sizes
ico_image = Image.new('RGBA', (len(image_sizes) * max_width, max_height))

# Generate images in different sizes and paste them into the ICO image
x_offset = 0
for size in image_sizes:
    new_image = Image.new('RGBA', size, (255, 255, 255, 0))  # Create a transparent image
    ico_image.paste(new_image, (x_offset, 0))
    x_offset += size[0]

# Save the ICO image with multiple sizes
ico_image.save('./tmp/scalable.ico')