from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the image size and color palette
width, height = 100, 100
palette = [
    0, 0, 0,  # Black
    255, 0, 0,  # Red
    0, 255, 0,  # Green
    0, 0, 255,  # Blue
    255, 255, 0,  # Yellow
]

# Create a new palette-based image
image = Image.new("P", (width, height))
image.putpalette(palette)

# Draw some shapes using the palette's colors
for y in range(height):
    for x in range(width):
        # Use a simple pattern to use colors from the palette
        image.putpixel((x, y), (x + y) % len(palette) // 3)

# Save the image
image.save('./tmp/palette_based_image.png')