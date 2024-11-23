import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the MIF file content
mif_content = """MIFVersion 5.5
Document
ViewSet 1
""Version Compatibility"" 10."""

# Save the MIF file
with open('./tmp/version_compatibility.mif', 'w') as file:
    file.write(mif_content)