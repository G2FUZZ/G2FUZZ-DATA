from PIL import Image
from PIL.TiffTags import TAGS_V2

# Create a new image with RGBA mode (4 layers: Red, Green, Blue, Alpha)
image = Image.new('RGBA', (100, 100))

# Add custom tags to the image
custom_tags = {
    40001: 'Custom Value 1',  # CustomTag1
    40002: 'Custom Value 2'   # CustomTag2
}

# Save the image with layers and custom tags as a TIFF file
image.save('./tmp/multi_layer_image_with_custom_tags.tiff', format='TIFF', tiffinfo=custom_tags)