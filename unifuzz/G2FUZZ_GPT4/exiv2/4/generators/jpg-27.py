from PIL import Image

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a blank image
image = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Saving the image in JPEG 2000 format with scalable resolutions
# To achieve the 'Scalable Resolutions (JPEG 2000)' feature, we use the JPEG 2000 format.
# Note: The file extension for JPEG 2000 is '.jp2' and not '.jpg'
image.save('./tmp/image_with_scalable_resolutions.jp2', 'JPEG2000')

print("Image saved to ./tmp/image_with_scalable_resolutions.jp2 with 'Scalable Resolutions (JPEG 2000)' feature.")