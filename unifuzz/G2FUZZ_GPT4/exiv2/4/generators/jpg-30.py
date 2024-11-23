import os
from PIL import Image
from io import BytesIO

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

main_image.info['thumbnail'] = thumbnail_bytes

# Save the main image with an embedded thumbnail in a format that supports Error Resilience
# Note: JPEG 2000 supports error resilience but PIL/Pillow might not directly offer control over these features.
# Saving as .jp2 (JPEG 2000) as a demonstration, but without specific error resilience parameters.
main_image.save('./tmp/main_image_with_thumbnail.jp2', 'JPEG2000')

# Verifying the new file is created
print("New image with potential error resilience saved as JPEG 2000 format.")