from PIL import Image, ImageDraw

# Create a black image with white text
image = Image.new('RGB', (100, 50), color='black')
text = "Lossless Rotation"
draw = ImageDraw.Draw(image)
draw.text((10, 10), text, fill='white')

# Add a more complex structure to the image by including additional marker segments and custom metadata
metadata_length = 30
metadata = b'Additional Metadata: Hello, World!'
image.info["APP1"] = metadata_length.to_bytes(2, byteorder='big') + metadata

# Multiple image data segments (fake image data)
for i in range(3):
    image.info["DQT" + str(i)] = bytes([0x00, 0x43]) + bytes(range(64))

# Save the image with the added complex structure
image.save('./tmp/lossless_rotation_with_complex_structure.jpg')