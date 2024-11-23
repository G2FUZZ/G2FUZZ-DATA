import struct

# Define the hotspot information
x_hotspot = 10
y_hotspot = 10

# Create the ICO file format data
icon_data = bytearray(
    struct.pack('<H', 0) +  # Reserved, must be 0
    struct.pack('<H', 2) +  # Image type: 1 for icon, 2 for cursor
    struct.pack('<H', 1) +  # Number of images in the file
    struct.pack('B', 32) +  # Image width
    struct.pack('B', 32) +  # Image height
    struct.pack('B', 0) +   # Number of colors in the color palette
    struct.pack('B', 0) +   # Reserved, must be 0
    struct.pack('<H', x_hotspot) +  # X coordinate of the hotspot
    struct.pack('<H', y_hotspot)    # Y coordinate of the hotspot
)

# Save the ICO file
with open('./tmp/hotspot_icon.ico', 'wb') as f:
    f.write(icon_data)

print("Hotspot ICO file generated and saved successfully.")