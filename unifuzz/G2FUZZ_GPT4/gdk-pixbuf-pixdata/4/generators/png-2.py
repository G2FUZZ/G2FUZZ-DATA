import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGBA mode (supporting transparency)
image_size = (200, 200)  # Example size
image = Image.new("RGBA", image_size)

# Example drawing: a semi-transparent square and a fully transparent circle
# Using a loop for simplicity; for complex shapes, consider using ImageDraw module

# Draw semi-transparent square
for x in range(50, 150):
    for y in range(50, 150):
        image.putpixel((x, y), (255, 0, 0, 128))  # Red, half-transparent

# Draw fully transparent circle
radius = 50
center = (100, 100)  # Center of the circle
for x in range(image_size[0]):
    for y in range(image_size[1]):
        if (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2:
            image.putpixel((x, y), (0, 0, 0, 0))  # Fully transparent

# Save the image
image.save('./tmp/transparent_example.png')