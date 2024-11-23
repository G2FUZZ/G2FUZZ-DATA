from PIL import Image
import os
import random

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with advanced features
image_width = random.randint(800, 1920)
image_height = random.randint(600, 1080)
compression_level = random.randint(1, 10)  # 1 (low quality) to 10 (high quality)
metadata = {'Author': 'John Doe', 'Date': '2023-01-15', 'Description': 'Randomly generated image'}

# Create a new image with random dimensions and white background
image = Image.new('RGB', (image_width, image_height), 'white')

# Set metadata for the image
image.info['icc_profile'] = b'ICC_PROFILE_DATA'
image.info['dpi'] = (300, 300)
image.info['exif'] = b'EXIF_DATA'

# Save the image with specified compression level and metadata
icc_profile = image.info.get('icc_profile')
dpi = image.info.get('dpi')
exif = image.info.get('exif')

image.save('./tmp/generated_complex_file.jpg', quality=compression_level, icc_profile=icc_profile, dpi=dpi, exif=exif)

print('JPG file with advanced features generated successfully!')