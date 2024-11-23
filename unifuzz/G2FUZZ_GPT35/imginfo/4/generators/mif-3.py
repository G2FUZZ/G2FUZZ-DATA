import os

# Define the graphics data
graphics_data = """
WIDTH=8;
DEPTH=256;

ADDRESS_RADIX=HEX;
DATA_RADIX=HEX;

CONTENT BEGIN
"""

# Add graphics data to the mif file
for i in range(256):
    graphics_data += f"{i:02X} : {i:02X};\n"

graphics_data += "END;"

# Save the graphics data to a mif file
file_path = "./tmp/graphics_data.mif"
with open(file_path, "w") as file:
    file.write(graphics_data)

print(f"Graphics data saved to: {file_path}")