import struct

# Define the ICO file header
ico_header = bytes([
    0, 0, 1, 0, 1, 0, 2, 0, 1, 0,
    32, 0  # 32-bit icon
])

# Define the icon image data
icon_data = bytes([
    40, 0, 0, 0, 40, 0, 0, 0, 64, 0, 0, 0, 64, 0, 0, 0, 1, 0, 32, 0, 3, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 40,
    0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0,
    0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40,
    0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0,
    0, 0, 0, 40, 0, 0
])

# Create the ICO file by combining the header and image data
ico_content = ico_header + icon_data

# Save the ICO file
with open('./tmp/custom_icon.ico', 'wb') as file:
    file.write(ico_content)

print("Custom icon file generated successfully!")