from PIL import Image
import io
import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Create a simple image using PIL
img = Image.new('RGB', (100, 100), color=(73, 109, 137))

# Save the image temporarily to a buffer
buffer = io.BytesIO()
img.save(buffer, format="JPEG")

# The attempt to add Exif data directly via Pillow without using an external library like piexif is not shown here
# because Pillow does not provide a straightforward method to create and embed Exif data from scratch.

# Save image to file
with open('./tmp/image_with_exif.jpg', 'wb') as img_file:
    img_file.write(buffer.getvalue())

print('Image saved to ./tmp/image_with_exif.jpg')