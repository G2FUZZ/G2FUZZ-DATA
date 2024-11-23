import os
from PIL import Image

# Create the ./tmp/ directory if it doesn't exist
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the image size and colors
width, height = 100, 100
background_color = (255, 0, 0, 0)  # Red with full transparency
circle_color = (0, 255, 0, 255)  # Green with no transparency

# Create a new image with transparency (RGBA mode for 32-bit images)
image = Image.new("RGBA", (width, height), background_color)

# Draw a circle in the middle
for y in range(height):
    for x in range(width):
        # Calculate the distance to the center
        distance_to_center = ((x - width / 2) ** 2 + (y - height / 2) ** 2) ** 0.5
        # If the distance is less than a threshold, color the pixel
        if distance_to_center < 30:
            image.putpixel((x, y), circle_color)

# Save the image with transparency
image.save(output_dir + 'transparent_image.bmp')