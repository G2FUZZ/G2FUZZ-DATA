import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Create a new image with RGBA (Red, Green, Blue, Alpha) mode for transparency
# Size: 400x400, Color: Transparent (0, 0, 0, 0)
image = Image.new("RGBA", (400, 400), (0, 0, 0, 0))

# Draw a semi-transparent red square in the center
for x in range(100, 300):
    for y in range(100, 300):
        # Setting the red square to be semi-transparent (128 out of 255 for alpha)
        image.putpixel((x, y), (255, 0, 0, 128))

# Save the image
image.save('./tmp/transparent_square.png')