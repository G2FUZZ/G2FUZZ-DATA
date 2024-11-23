from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a simple image with a gradient
width, height = 800, 600
image = Image.new('RGB', (width, height), "#FFFFFF")
draw = ImageDraw.Draw(image)
for i in range(height):
    gradient = int((i / height) * 255)
    draw.line([(0, i), (width, i)], fill=(gradient, gradient, gradient))

# Save the image with high-quality level (e.g., 95)
image.save('./tmp/high_quality.jpg', 'JPEG', quality=95)

# Save the same image with a lower quality level (e.g., 30)
image.save('./tmp/low_quality.jpg', 'JPEG', quality=30)