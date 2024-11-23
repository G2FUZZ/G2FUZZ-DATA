import os
from PIL import Image
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

# It's not typical to embed the raw thumbnail bytes directly into the image info like this,
# as the info dictionary is used for metadata such as EXIF. Instead, you might save the thumbnail
# alongside the main image or use a proper metadata format to embed thumbnails.
# However, for demonstration purposes and to keep the structure of your code, we proceed as follows:
main_image.info['thumbnail'] = thumbnail_bytes

# To demonstrate the Lossless and Lossy Compression Modes feature of JPEG 2000,
# we will save the main image in JPEG 2000 format, which supports both compression modes.
# While the PIL library does not directly allow specifying the mode in the save function,
# choosing JPEG 2000 format (.jp2) inherently enables the use of both compression modes.
# This is a simplification for demonstration; in practice, you might specify compression settings directly
# if your image processing library supports it.
main_image.save('./tmp/main_image_with_lossless_lossy.jp2', 'JPEG2000')

# Verifying the thumbnail is embedded by loading the image again
loaded_image = Image.open('./tmp/main_image_with_lossless_lossy.jp2')
print("Thumbnail embedded:", 'thumbnail' in loaded_image.info)

# Note: The code above saves the main image in JPEG 2000 format, which supports both lossless and
# lossy compression modes. However, embedding raw thumbnail bytes in the image info and expecting
# it to be preserved exactly as-is might not work as expected with JPEG 2000 format or might not be
# supported by all image viewers or processors. This demonstration focuses on the format's capabilities
# rather than practical metadata embedding techniques, which would typically use standardized metadata formats.