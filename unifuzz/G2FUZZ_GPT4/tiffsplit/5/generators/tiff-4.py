from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new("RGB", (100, 100), color=(255, 0, 0))

# Define metadata
metadata = {
    "ImageDescription": "Sample TIFF image with metadata",
    "XResolution": (300, 1),
    "YResolution": (300, 1),
    "ResolutionUnit": 2,  # 2 indicates that the resolution is in pixels/inch
}

# Pillow's save method does not directly accept metadata for all tags,
# so we need to use TiffImagePlugin's IFD class to add custom metadata.
info = TiffImagePlugin.ImageFileDirectory_v2()

# Add metadata to the IFD
for tag, value in metadata.items():
    if tag in TiffTags.TAGS_V2:
        tag_id = TiffTags.TAGS_V2[tag]
        info[tag_id] = value
    else:
        print(f"Warning: Tag '{tag}' not found in TiffTags.TAGS_V2. Skipping.")

# Save the image with metadata
image.save('./tmp/sample_with_metadata.tiff', tiffinfo=info)