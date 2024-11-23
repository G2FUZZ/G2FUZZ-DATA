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

# Save the main image with an embedded thumbnail
main_image.save('./tmp/main_image_with_thumbnail.jpg', 'JPEG')

# Verifying the thumbnail is embedded by loading the image again
loaded_image = Image.open('./tmp/main_image_with_thumbnail.jpg')
print("Thumbnail embedded:", 'thumbnail' in loaded_image.info)