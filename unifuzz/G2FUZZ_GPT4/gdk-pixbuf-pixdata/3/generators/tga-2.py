from PIL import Image

# Create an RGBA image (Red, Green, Blue, Alpha)
width, height = 256, 256
image = Image.new("RGBA", (width, height))

# Draw a gradient from opaque to transparent
for y in range(height):
    for x in range(width):
        # Gradient in red channel, constant green and blue, alpha fading from 255 to 0
        red = x
        green = 128
        blue = 128
        alpha = 255 - int((y / height) * 255)
        image.putpixel((x, y), (red, green, blue, alpha))

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image as TGA
image.save('./tmp/gradient_with_alpha.tga')

print("TGA file with alpha channel created successfully.")