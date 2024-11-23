from PIL import Image

# Define the image size and color depth
width, height = 400, 200
color = (255, 0, 0, 255)  # Red with full opacity

# Create a new image with RGBA mode (Red, Green, Blue, Alpha)
image = Image.new("RGBA", (width, height))

# Apply a gradient of transparency
for x in range(width):
    for y in range(height):
        # Modify the alpha value to create a transparency gradient
        alpha = int(255 * (x / width))
        image.putpixel((x, y), (color[0], color[1], color[2], alpha))

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image
image.save('./tmp/gradient_with_alpha.bmp')

print("Image with alpha channel saved.")