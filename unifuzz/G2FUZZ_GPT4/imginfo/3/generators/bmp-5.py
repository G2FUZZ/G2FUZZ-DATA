from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Create a new image with RGB mode
width, height = 640, 480
image = Image.new('RGB', (width, height), "blue")  # A blue image

# Optionally, draw some graphics on the image for demonstration
# For simplicity, let's draw a red rectangle
from PIL import ImageDraw

draw = ImageDraw.Draw(image)
draw.rectangle([200, 150, 440, 330], fill="red")

# Save the image as BMP which inherently includes a DIB header for device independence
image.save('./tmp/demo_image.bmp')

print("Image saved to ./tmp/demo_image.bmp")