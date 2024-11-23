import os
import struct

# Create a directory to store the generated ICO files
os.makedirs("./tmp/", exist_ok=True)

# Define the frames for the animated icon
frame1 = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x06\x00\x00\x00\x22\x22\x00\x00\x00\x00\x00\x00\x01\x00\x18\x00'
frame2 = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x06\x00\x00\x00\x22\x22\x00\x00\x00\x00\x00\x00\x01\x00\x18\x00'

# Combine the frames to create the animated icon
icon_data = frame1 + frame2

# Write the icon data to a .ico file
with open("./tmp/animated_icon.ico", "wb") as file:
    file.write(icon_data)

print("Animated icon file generated successfully.")