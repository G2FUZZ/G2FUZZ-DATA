from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with mode 'RGB' and white background
width, height = 100, 100
image = Image.new('RGB', (width, height))

# Draw a gradient from black to white
for x in range(width):
    for y in range(height):
        # Calculate the brightness as a function of the position
        brightness = int((x / width) * 255)
        # Set the pixel color to the calculated brightness value
        image.putpixel((x, y), (brightness, brightness, brightness))

# Save the image
image.save('./tmp/gradient.bmp')