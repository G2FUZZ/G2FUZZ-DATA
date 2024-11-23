from PIL import Image, ImageDraw

# Create an image with RGB mode
width, height = 300, 300
image = Image.new("RGB", (width, height), "white")

# Create a draw object to add elements to the image
draw = ImageDraw.Draw(image)

# Generate a vertical gradient
for i in range(height):
    gradient_color = int(255 * (i / height))  # Calculate the color
    draw.line((0, i, width, i), fill=(gradient_color, gradient_color, gradient_color))

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as progressive JPEG
image.save('./tmp/progressive_image.jpg', 'JPEG', quality=80, progressive=True)