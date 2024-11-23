import os
from PIL import Image

# Create a directory for saving the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample image
image = Image.new('RGB', (100, 100), color='red')

# Save the image with different quality settings
qualities = [50, 70, 90]
for i, quality in enumerate(qualities):
    image.save(f'./tmp/quality_{i+1}.jpg', quality=quality)