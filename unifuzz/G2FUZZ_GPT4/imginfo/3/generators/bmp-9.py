import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image without layers or animation, as BMP doesn't support them
# Setting up the image dimensions and color (RGB tuple)
image_width, image_height = 640, 480
background_color = (255, 0, 0)  # Red background

# Create a new image with the specified background color
image = Image.new('RGB', (image_width, image_height), color=background_color)

# Save the image as BMP
image_path = './tmp/static_image.bmp'
image.save(image_path)

print(f"Image saved at {image_path}")