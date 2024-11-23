from PIL import Image, ImageDraw, ImageFont, TiffTags, TiffImagePlugin
import os

# Ensure tmp directory exists
os.makedirs('./tmp', exist_ok=True)

# Create a new image with white background
img = Image.new('RGB', (800, 600), color=(255, 255, 255))

# Initialize ImageDraw
d = ImageDraw.Draw(img)

# Optionally, add some text to simulate a scanned document
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 30)
d.text((10,10), "This is a sample scanned document.", fill=(0,0,0), font=font)

# Define custom and SMinSampleValue and SMaxSampleValue tags
custom_tag_id = 65000
custom_tag_value = b"CustomInfo"  # The value must be bytes
smin_sample_value_tag_id = 340
smax_sample_value_tag_id = 341

# Define the SMinSampleValue and SMaxSampleValue. For simplicity, let's assume our image uses 8-bit samples.
# Thus, the valid range is 0 to 255 for each component in RGB.
smin_sample_value = (0, 0, 0)  # Minimum for RGB
smax_sample_value = (255, 255, 255)  # Maximum for RGB

# Before saving, let's add our custom tag to the image
if hasattr(TiffImagePlugin, 'WRITE_LIBTIFF') and TiffImagePlugin.WRITE_LIBTIFF:
    # If the PIL version supports it and libtiff is available, use the libtiff extension
    info = TiffImagePlugin.ImageFileDirectory_v2()
    info[custom_tag_id] = (TiffTags.TYPES['byte'], 0, custom_tag_value, True)
    # Adding SMinSampleValue and SMaxSampleValue tags
    info[smin_sample_value_tag_id] = (TiffTags.TYPES['short'], len(smin_sample_value), smin_sample_value, False)
    info[smax_sample_value_tag_id] = (TiffTags.TYPES['short'], len(smax_sample_value), smax_sample_value, False)
    img.save('./tmp/sample_scanned_document_with_additional_tags.tiff', "TIFF", tiffinfo=info)
else:
    # Fallback: if the PIL version does not support custom tags through libtiff
    print("Note: Custom tags support requires a PIL version that supports writing through libtiff.")
    img.save('./tmp/sample_scanned_document_with_additional_tags.tiff', "TIFF")

print(f"TIFF file with custom and SMinSampleValue and SMaxSampleValue tags saved at: './tmp/sample_scanned_document_with_additional_tags.tiff'")