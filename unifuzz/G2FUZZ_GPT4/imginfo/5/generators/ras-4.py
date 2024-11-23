from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a simple image using PIL
# Here, we create a 100x100 red image for demonstration
image = Image.new('RGB', (100, 100), "red")

# Save the image in a supported format, e.g., PNG
image.save(output_dir + 'example.png', format='PNG')