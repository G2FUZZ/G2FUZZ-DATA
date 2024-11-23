from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with gradient
width, height = 256, 256
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

# Generate a gradient with more colors than GIF supports
for i in range(width):
    for j in range(height):
        r = (i + j) % 256
        g = (i * 2 + j * 2) % 256
        b = (i * 3 + j * 3) % 256
        draw.point((i, j), (r, g, b))

# Convert the image to use a 256 color palette
image = image.convert("P", palette=Image.ADAPTIVE, colors=256)

# Save the image as a GIF
image.save('./tmp/gradient_color_limit.gif')