import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the mif file
mif_content = """
WIDTH=16;
DEPTH=256;
ADDRESS_RADIX=HEX;
DATA_RADIX=HEX;

CONTENT BEGIN
"""

# Generate content for the mif file
for i in range(256):
    mif_content += f"    {i:02X} : {i:02X};\n"

# End of the mif file content
mif_content += "END;"

# Save the content to a mif file
with open('./tmp/data.mif', 'w') as file:
    file.write(mif_content)

print('MIF file generated successfully!')