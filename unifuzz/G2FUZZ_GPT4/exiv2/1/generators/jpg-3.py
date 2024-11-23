from PIL import Image, ExifTags, PngImagePlugin
import os

# Create the 'tmp' directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Create a blank image
img = Image.new('RGB', (100, 100), color='red')

# Prepare basic metadata (not detailed EXIF, as that's more complex)
metadata = PngImagePlugin.PngInfo()
metadata.add_text('DateTime', '2023:01:01 00:00:00')
metadata.add_text('Make', 'PIL Fake Camera')
metadata.add_text('Model', 'PIL Model 1')
# Note: GPSInfo and other detailed EXIF data cannot be directly added this way

# Saving the image with basic metadata
img.save('./tmp/exif_example.jpg', pnginfo=metadata)