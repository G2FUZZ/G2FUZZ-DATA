import os

# Create a directory for storing generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the file footer
file_footer = b'\x00\x00\x00\x00\x00\x00\x00\x00TRUEVISION-XFILE.'

# Generate a TGA file with the specified file footer
with open('./tmp/generated_file.tga', 'wb') as f:
    # Write the actual image data (not included in this example)
    
    # Write the file footer at the end of the file
    f.write(file_footer)