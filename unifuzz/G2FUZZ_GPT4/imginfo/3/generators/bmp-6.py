from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an RGBA image with a transparent gradient
width, height = 200, 200
image = Image.new('RGBA', (width, height))

# Create a transparent gradient
for x in range(width):
    for y in range(height):
        # Calculate the transparency level
        alpha = int(255 * (x / width))
        # Set the pixel to a specific color with the calculated transparency
        image.putpixel((x, y), (255, 105, 180, alpha))  # Pink with variable transparency

# Save the image
image.save('./tmp/transparent_image.bmp')

print("The BMP image with transparency has been saved to ./tmp/transparent_image.bmp")