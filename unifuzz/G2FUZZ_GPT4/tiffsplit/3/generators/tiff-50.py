from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define custom tag IDs, must be in the private range (>= 32768)
CUSTOM_TAGS = {
    "CustomTag1": 32768,
    "CustomTag2": 32769,
}

# Register custom tags with PIL
TiffTags.TAGS_V2.update(CUSTOM_TAGS)
TiffImagePlugin.WRITE_LIBTIFF = True

# Function to create an IFD (Image File Directory) for a TIFF tag
def create_ifd(tag, value):
    ifd = TiffImagePlugin.ImageFileDirectory_v2()
    ifd[tag] = value
    return ifd

# Create multiple images and assign metadata
images = [
    Image.new('RGB', (800, 600), color=(255, 0, 0)),
    Image.new('RGB', (800, 600), color=(0, 255, 0)),
    Image.new('RGB', (800, 600), color=(0, 0, 255)),
]

metadata_list = [
    {
        "image_description": "Red page",
        "x_resolution": (300, 1),
        "y_resolution": (300, 1),
        "software": "Pillow",
        "customtag1": "Custom data for red page",
    },
    {
        "image_description": "Green page",
        "x_resolution": (300, 1),
        "y_resolution": (300, 1),
        "software": "Pillow",
        "customtag2": "Custom data for green page",
    },
    {
        "image_description": "Blue page",
        "x_resolution": (300, 1),
        "y_resolution": (300, 1),
        "software": "Pillow",
        "customtag1": "Custom data for blue page",
        "customtag2": "Another piece of custom data for blue page",
    },
]

# Prepare IFDs for each page
ifds = []
for metadata in metadata_list:
    info = TiffImagePlugin.ImageFileDirectory_v2()
    for tag, value in metadata.items():
        tag_code = TiffTags.TAGS_V2.get(tag.lower())  # Ensure tag lookup is case-insensitive
        if tag_code:
            info[tag_code] = value
    ifds.append(info)

# Save the images as a multi-page TIFF
with TiffImagePlugin.AppendingTiffWriter('./tmp/multi_page_with_metadata.tiff', True) as tf:
    for i, image in enumerate(images):
        image.save(tf, format='TIFF', tiffinfo=ifds[i], save_all=True)
        tf.newFrame()

print("Multi-page TIFF with metadata and custom tags saved successfully.")