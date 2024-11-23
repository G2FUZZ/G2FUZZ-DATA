import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Define the dimensions of the image
width = 800
height = 600

# Create a blank RGB image
image = np.zeros((height, width, 3), dtype=np.uint8)

# Add a gradient background
for x in range(width):
    for y in range(height):
        image[y, x] = [x % 256, y % 256, (x + y) % 256]

# Create a PIL image from the numpy array
img = Image.fromarray(image)

# Add shapes to the image
draw = ImageDraw.Draw(img)
draw.rectangle([100, 100, 300, 300], fill=(255, 0, 0))
draw.ellipse([400, 100, 600, 300], fill=(0, 255, 0))

# Add text to the image
text = "Complex Generated Image"
draw.text((50, 50), text, fill=(255, 255, 255))

# Apply a filter effect
img = img.filter(ImageFilter.GaussianBlur(radius=2))

# Create another layer with a transparent circle
overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.ellipse([200, 400, 600, 550], fill=(255, 255, 255, 128))

# Composite the overlay onto the main image
img = Image.alpha_composite(img.convert('RGBA'), overlay)

# Convert the image to RGB mode before saving
img = img.convert('RGB')

# Save the image to a file
img.save('./tmp/complex_image_extended.jpg')

print("Complex Image with Extended Features saved successfully.")