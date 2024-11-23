import io
from PIL import Image

# Create a new ICO file
ico_data = b'\x00\x00\x01\x00'  # ICO header
image_data = b''  # Image data

# Create a 32x32 image with RGBA color
image = Image.new('RGBA', (32, 32), color='red')
output = io.BytesIO()
image.save(output, format='ICO')
image_data += output.getvalue()

# Create a 64x64 image with RGBA color
image = Image.new('RGBA', (64, 64), color='green')
output = io.BytesIO()
image.save(output, format='ICO')
image_data += output.getvalue()

# Save the ICO file
with open('./tmp/icon.ico', 'wb') as f:
    f.write(ico_data + image_data)