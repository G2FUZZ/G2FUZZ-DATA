import io
from PIL import Image

# Create new ICO file
ico_data = b'\x00\x00\x01\x00'  # ICO header
image_data = b''  # Image data

# Create sample image
image = Image.new('RGB', (32, 32), color='red')
output = io.BytesIO()
image.save(output, format='BMP')
bmp_data = output.getvalue()

# Add image data to ICO file
image_entry = bytearray(bmp_data)
image_data += image_entry

# Save ICO file
with open('./tmp/icon.ico', 'wb') as f:
    f.write(ico_data + image_data)