import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with RGBA (Red, Green, Blue, Alpha) values
width, height = 200, 200
image = Image.new("RGBA", (width, height))

# Generate a gradient with varying alpha values
for x in range(width):
    for y in range(height):
        # Calculate the alpha value as a gradient based on the y coordinate
        alpha = int(255 * (y / height))
        # Set a blue color with the calculated alpha
        image.putpixel((x, y), (0, 0, 255, alpha))

# Save the image with an alpha channel
image.save('./tmp/alpha_gradient.bmp', "BMP")

print("Image with alpha channel saved.")