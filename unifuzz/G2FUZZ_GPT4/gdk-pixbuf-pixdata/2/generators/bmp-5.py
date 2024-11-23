import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA (Red, Green, Blue, Alpha) support
# Setting the image size to 100x100 and the color to red with 50% transparency
image = Image.new("RGBA", (100, 100), (255, 0, 0, 128))

# Save the image with alpha channel as BMP
# Note: BMP's support for alpha channels might not be recognized by all viewers
image.save('./tmp/alpha_channel_example.bmp')

print("BMP file with alpha channel saved.")