from PIL import Image, ExifTags
import os
import io

# Create a directory for the output if it doesn't exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)  # Corrected variable name here

# Create a simple image
image = Image.new('RGB', (100, 100), color = 'red')

# Save image without Exif data due to the complexity of correctly handling Exif bytes
file_path = os.path.join(output_dir, 'image_without_exif.jpg')
image.save(file_path, 'JPEG')

print(f"Image saved at {file_path}")