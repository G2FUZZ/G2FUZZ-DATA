import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a main image (example: 800x600, blue background)
main_image = Image.new('RGB', (800, 600), color = 'blue')

# Create a thumbnail of the main image (example: 80x60)
thumbnail = main_image.copy()  # Corrected the variable name here
thumbnail.thumbnail((80, 60))

# Save the main image
main_image_path = './tmp/main_image.jpg'
main_image.save(main_image_path)

# Save the thumbnail image
thumbnail_path = './tmp/thumbnail.jpg'
thumbnail.save(thumbnail_path)