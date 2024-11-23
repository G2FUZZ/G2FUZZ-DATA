import os
from PIL import Image, ImageFile
from io import BytesIO  # Import BytesIO for in-memory bytes handling

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create the main image
main_image = Image.new('RGB', (800, 600), color='blue')

# Create a smaller thumbnail image
thumbnail = Image.new('RGB', (80, 60), color='green')

# Convert the thumbnail to JPEG bytes using a BytesIO object
thumbnail_bytes_io = BytesIO()  # Create a BytesIO object
thumbnail.save(thumbnail_bytes_io, format='JPEG')  # Save the thumbnail to the BytesIO object in JPEG format
thumbnail_bytes = thumbnail_bytes_io.getvalue()  # Retrieve the bytes value of the thumbnail

# Embed the thumbnail in the main image info (not typical for production use)
main_image.info['thumbnail'] = thumbnail_bytes

# Save the main image with an embedded thumbnail and optimized Huffman tables
# PILLOW doesn't expose Huffman table optimization directly in the high-level API.
# However, it automatically optimizes Huffman tables for the size when saving JPEGs.
# For explicit control, one would typically need to manipulate the JPEG encoder or use a different library.
# Since PILLOW abstracts away such low-level details, we'll proceed with the default behavior,
# which includes optimized Huffman tables as part of the JPEG saving process.

# The optimize parameter can be used to further instruct PIL to optimize the image before saving
main_image.save('./tmp/main_image_with_thumbnail_optimized.jpg', 'JPEG', optimize=True)

# Verifying the thumbnail is embedded by loading the image again
loaded_image = Image.open('./tmp/main_image_with_thumbnail_optimized.jpg')
print("Thumbnail embedded:", 'thumbnail' in loaded_image.info)