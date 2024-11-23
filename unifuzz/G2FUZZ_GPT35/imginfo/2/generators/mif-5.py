import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file content
mif_content = """
HIERARCHICAL:
SUPPORTS A HIERARCHICAL STRUCTURE FOR ORGANIZING DOCUMENT ELEMENTS
"""

# Save the generated mif file
file_path = './tmp/features.mif'
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"Generated mif file saved at: {file_path}")