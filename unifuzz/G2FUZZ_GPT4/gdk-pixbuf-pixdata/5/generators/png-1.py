from PIL import Image, ImageDraw

# Create an image with mode 'RGBA' (Red, Green, Blue, Alpha) and white background
image_size = (200, 200)
image = Image.new("RGBA", image_size, "white")

# Draw a simple pattern on the image
draw = ImageDraw.Draw(image)
for i in range(0, 200, 10):
    draw.line((i, 0, i, 200), fill="black", width=1)
    draw.line((0, i, 200, i), fill="black", width=1)

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the image with lossless compression
image_path = './tmp/lossless_compression_example.png'
image.save(image_path, "PNG")

print(f"Image saved at {image_path}")