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

# Define custom tags (as per TIFF spec, custom tags should use the range 33000-65535)
# Here, we define a simple tag to demonstrate. Let's use tag 65000 for this example
# The format we choose is '1s' which means a single string. Other formats are available depending on the data type.
custom_tag_id = 65000
custom_tag_value = b"CustomInfo"  # The value must be bytes

# Before saving, let's add our custom tag to the image and specify endianness
if hasattr(TiffImagePlugin, 'WRITE_LIBTIFF') and TiffImagePlugin.WRITE_LIBTIFF:
    # If the PIL version supports it and libtiff is available, use the libtiff extension
    info = TiffImagePlugin.ImageFileDirectory_v2()
    info[custom_tag_id] = (TiffTags.TYPES['byte'], 0, custom_tag_value, True)
    
    # Adding Predictor Compression
    # TIFFTAG_PREDICTOR value is 317
    # For LZW Compression, use predictor value 2 (horizontal differencing)
    info[317] = 2  # Predictor tag
    
    # Endianness flexibility: Specify the byte order
    # 'II' for little-endian (Intel style)
    # 'MM' for big-endian (Motorola style)
    # This example demonstrates saving in both formats; choose one as needed.
    # To save in little-endian format with Predictor Compression:
    img.save('./tmp/sample_scanned_document_with_custom_tags_little_endian_predictor.tiff', "TIFF", tiffinfo=info, save_all=True, compression="tiff_lzw", endian='II')
    print("TIFF file with custom tags and Predictor Compression saved in little-endian format at: './tmp/sample_scanned_document_with_custom_tags_little_endian_predictor.tiff'")
    
    # To save in big-endian format with Predictor Compression:
    img.save('./tmp/sample_scanned_document_with_custom_tags_big_endian_predictor.tiff', "TIFF", tiffinfo=info, save_all=True, compression="tiff_lzw", endian='MM')
    print("TIFF file with custom tags and Predictor Compression saved in big-endian format at: './tmp/sample_scanned_document_with_custom_tags_big_endian_predictor.tiff'")
else:
    # Fallback: if the PIL version does not support custom tags through libtiff, 
    # we'll have to rely on PIL's standard mechanism without custom tags or implement another approach.
    print("Note: Custom tags and Predictor Compression support requires a PIL version that supports writing through libtiff.")
    # Fallback does not support endianness specification or Predictor Compression, so we just save it without specifying these features.
    img.save('./tmp/sample_scanned_document_with_custom_tags_predictor.tiff', "TIFF")
    print(f"TIFF file with custom tags and possibly without proper Predictor Compression support saved at: './tmp/sample_scanned_document_with_custom_tags_predictor.tiff'")