import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new blank (white) 32x32 pixel image
image = Image.new("RGBA", (32, 32), "white")
draw = ImageDraw.Draw(image)

# Draw a simple element to represent the cursor - here, a black dot
draw.ellipse((14, 14, 18, 18), fill="black")

# Hotspot coordinates for the cursor
x_hotspot, y_hotspot = 10, 10

# CUR file header specific settings
# This includes the magic number, image type (2 for .cur), image count (1),
# and the specific bytes that define the image dimensions, color depth,
# and hotspot coordinates.
cur_header = bytes([
    0x00, 0x00, # Reserved
    0x02, 0x00, # Type (2 for .cur)
    0x01, 0x00, # Image count (1)
    32, 32, # Width, Height
    0x00, # Colors (0 = no palette)
    0x00, # Reserved
    x_hotspot & 0xFF, x_hotspot >> 8, # X hotspot
    y_hotspot & 0xFF, y_hotspot >> 8, # Y hotspot
    32, 32, 0x00, 0x00, # Width, Height (again), and planes
    32, 0x00, 0x00, 0x00, # Bit count and size of the bitmap data in bytes
    22, 0x00, 0x00, 0x00, # Offset of bitmap data
])

# Convert the image to RGBA format and get the raw bytes
image_bytes = image.convert("RGBA").tobytes()

# The size of the image data in bytes
image_size = len(image_bytes)

# Append the actual image data to the file content
file_content = cur_header + image_bytes

# Save the CUR file
cur_file_path = './tmp/cursor.cur'
with open(cur_file_path, 'wb') as f:
    f.write(file_content)

print(f"CUR file saved at {cur_file_path}")