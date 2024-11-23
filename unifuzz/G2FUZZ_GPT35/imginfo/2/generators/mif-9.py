import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the mif file
mif_content = """
DEPTH = 256;
WIDTH = 8;
ADDRESS_RADIX = HEX;
DATA_RADIX = HEX;
CONTENT BEGIN
"""

# Adding custom features to the mif file
mif_content += "    0 : 00;\n"
mif_content += "    1 : 01;\n"
mif_content += "    2 : 02;\n"
mif_content += "    3 : 03;\n"
mif_content += "    4 : 04;\n"
mif_content += "    5 : 05;\n"
mif_content += "    6 : 06;\n"
mif_content += "    7 : 07;\n"
mif_content += "    8 : 08;\n"

mif_content += "END;\n"

# Save the mif file
with open('./tmp/custom_features.mif', 'w') as f:
    f.write(mif_content)