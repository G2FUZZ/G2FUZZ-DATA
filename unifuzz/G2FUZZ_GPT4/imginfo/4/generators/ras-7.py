from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image (e.g., 100x100 pixels) with a solid color (e.g., red)
width, height = 100, 100
image = Image.new('RGB', (width, height), 'red')

# Save the image as a PNG file
image_path = './tmp/example.png'
image.save(image_path, format='PNG')  # Changed 'ras' to 'PNG'

print(f'Image saved as {image_path}')