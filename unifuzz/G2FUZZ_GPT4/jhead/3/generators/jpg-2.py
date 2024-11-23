from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image dimensions
width, height = 256, 100

# Create a new image with 24-bit color (RGB)
image = Image.new('RGB', (width, height))

# Generate a gradient demonstrating a range of colors
for x in range(width):
    for y in range(height):
        # Calculate color values to create a gradient effect
        red = int((x / width) * 255)
        green = int((y / height) * 255)
        blue = 255 - int((x / width) * 255)
        
        # Set the pixel to the calculated color value
        image.putpixel((x, y), (red, green, blue))

# Save the image as a JPEG file
image.save('./tmp/gradient_24bit.jpg', 'JPEG')

print("Image has been generated and saved to ./tmp/gradient_24bit.jpg")