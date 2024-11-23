from PIL import Image

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a blank image
image = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Note: The standard PIL library does not support creating JPEG images in lossless mode directly.
# JPEG lossless mode is not commonly used and is not supported by many image processing libraries,
# including PIL/Pillow. The lossless mode in JPEG (specified in JPEG extensions like JPEG-LS) requires
# specific encoding mechanisms that are not implemented in Pillow.

# For demonstration purposes, we'll save the image without applying lossless mode, as it's not supported.
# To achieve lossless compression with Pillow, one could use a format like PNG, which is inherently lossless.
image.save('./tmp/image_without_lossless_mode.jpg', 'JPEG')  # JPEG does not support a lossless mode in Pillow

print("Image saved to ./tmp/image_without_lossless_mode.jpg. Note: JPEG lossless mode is not supported in Pillow.")