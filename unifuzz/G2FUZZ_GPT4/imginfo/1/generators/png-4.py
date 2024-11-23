import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with white background
img_size = (200, 200)
image = Image.new('RGB', img_size, color='white')
draw = ImageDraw.Draw(image)

# Optional: Draw something on the image for visualization
# Here, drawing a simple house shape
draw.polygon([(100, 50), (150, 100), (50, 100)], outline='black', fill='blue')  # Roof
draw.rectangle([(50, 100), (150, 150)], outline='black', fill='green')  # Base

# Save the image with Adam7 interlacing
image.save('./tmp/interlaced_image.png', 'PNG', interlace=1)