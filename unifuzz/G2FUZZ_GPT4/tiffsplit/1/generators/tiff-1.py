from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument name here

# Create multiple images to be stored in a single TIFF file
image1 = Image.new('RGB', (100, 100), color = 'red')
image2 = Image.new('RGB', (100, 100), color = 'green')
image3 = Image.new('RGB', (100, 100), color = 'blue')

# Save the images as a multipage TIFF
image1.save('./tmp/multiple_images.tiff', save_all=True, append_images=[image2, image3])

print("TIFF file with multiple images created successfully.")