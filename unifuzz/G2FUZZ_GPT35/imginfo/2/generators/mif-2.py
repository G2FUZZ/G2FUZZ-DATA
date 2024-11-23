# Define the content of the 'mif' file
mif_content = """
Version 5
// MIF file for Desktop Publishing
// Purpose: Text-based format used to exchange information between different DTP applications

<Content here>

End of file
"""

# Save the content to a 'mif' file in the ./tmp/ directory
file_path = './tmp/example.mif'
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"Generated 'mif' file: {file_path}")