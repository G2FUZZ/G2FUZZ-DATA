import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file content with metadata and multiple sections
mif_content = """
TITLE: Complex MIF File
AUTHOR: John Doe
DATE: 2022-01-01

SECTION 1:
This is the content of section 1.

SECTION 2:
This is the content of section 2.
"""

# Save the generated mif file with more complex features
file_path = './tmp/complex_features.mif'
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"Generated complex mif file saved at: {file_path}")