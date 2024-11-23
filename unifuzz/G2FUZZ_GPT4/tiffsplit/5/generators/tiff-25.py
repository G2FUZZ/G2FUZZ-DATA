from PIL import Image, TiffTags, TiffImagePlugin
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image
image = Image.new("RGB", (100, 100), color=(255, 0, 0))

# Define metadata including Ink Names Tag and a placeholder for Security Tags
metadata = {
    "ImageDescription": "Sample TIFF image with metadata and security tags",
    "XResolution": (300, 1),
    "YResolution": (300, 1),
    "ResolutionUnit": 2,  # 2 indicates that the resolution is in pixels/inch
    "InkNames": "Cyan\Magenta\Yellow\Black",  # Ink Names for CMYK; note the use of backslash as specified in TIFF spec
    # Placeholder for Security Tags - this tag is fictional and for demonstration purposes only.
    # You may need to implement actual encryption or hashing mechanisms and store relevant data in custom tags.
    "SecurityTags": "Encrypted with AES256"
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
    elif tag == "SecurityTags":
        # Assuming 65000 as a custom tag ID for SecurityTags. In practice, choose an ID that does not conflict with existing standard tags.
        info[65000] = value
    else:
        print(f"Warning: Tag '{tag}' not found in TiffTags.TAGS_V2 and is not a custom tag. Skipping.")

# Save the image with metadata
image.save('./tmp/sample_with_metadata_security_tags.tiff', tiffinfo=info)