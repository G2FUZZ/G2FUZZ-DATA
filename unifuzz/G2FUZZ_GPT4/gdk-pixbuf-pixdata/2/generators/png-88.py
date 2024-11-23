import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate dummy image data to represent the concept of filtering
image_height = 200
image_width = 600
data = np.zeros((image_height, image_width, 4), dtype=np.uint8)  # Note the 4 for the alpha channel

# Divide the image into parts to represent different filters
filter_sections = image_width // 5

# Colors for different sections, now including an alpha value for transparency
colors = [
    (255, 0, 0, 255),
    (0, 255, 0, 200),  # Slightly transparent
    (0, 0, 255, 150),  # More transparent
    (255, 255, 0, 100),  # Even more transparent
    (0, 255, 255, 50)  # Most transparent
]

# Apply colors to different sections to represent filter types
for i, color in enumerate(colors):
    data[:, i*filter_sections:(i+1)*filter_sections] = color

# Convert the Numpy array to a PIL Image object and create a 'draw' object
image = Image.fromarray(data, 'RGBA')
draw = ImageDraw.Draw(image)

# Define text annotations and position them
filter_names = ['Red Filter', 'Green Filter', 'Blue Filter', 'Yellow Filter', 'Cyan Filter']
font = ImageFont.load_default()  # Using default font, replace with a path to a TrueType font for better control

for i, name in enumerate(filter_names):
    text_position = (i * filter_sections + 10, 10)  # Adjust as needed
    draw.text(text_position, name, fill='white', font=font)

# Create a gradient for an additional layer of complexity
for y in range(image_height):
    for x in range(image_width):
        current_color = image.getpixel((x, y))
        # Create a vertical gradient based on the y position
        gradient_factor = 255 - int((y / image_height) * 255)
        new_color = (current_color[0], current_color[1], current_color[2], gradient_factor)
        image.putpixel((x, y), new_color)

# Save the image to a file
image.save('./tmp/complex_png_filter_visualization.png')