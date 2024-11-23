from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Create a simple image using PIL
img = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Save the image with Adam7 interlacing
img.save('./tmp/interlaced_image.png', 'PNG', interlaced=True)