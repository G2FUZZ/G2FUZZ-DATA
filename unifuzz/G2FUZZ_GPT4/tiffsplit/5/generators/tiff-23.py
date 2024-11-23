from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new("RGB", (100, 100), color=(255, 0, 0))

# Define metadata including Ink Names Tag
metadata = {
    "ImageDescription": "Sample TIFF image with metadata",
    "XResolution": (300, 1),
    "YResolution": (300, 1),
    "ResolutionUnit": 2,  # 2 indicates that the resolution is in pixels/inch
    "InkNames": "Cyan\Magenta\Yellow\Black"  # Ink Names for CMYK; note the use of backslash as specified in TIFF spec
}

# Pillow's save method does not directly accept metadata for all tags,
# so we need to use TiffImagePlugin's IFD class to add custom metadata.
info = TiffImagePlugin.ImageFileDirectory_v2()

# Add metadata to the IFD
for tag, value in metadata.items():
    if tag in TiffTags.TAGS_V2:
        tag_id = TiffTags.TAGS_V2[tag]
        info[tag_id] = value
    elif tag == "InkNames":
        # For InkNames, the tag value is 33432 according to TIFF specification.
        info[33432] = value
    else:
        print(f"Warning: Tag '{tag}' not found in TiffTags.TAGS_V2 and is not a custom tag. Skipping.")

# Save the image with metadata
image.save('./tmp/sample_with_metadata_and_ink_names.tiff', tiffinfo=info)