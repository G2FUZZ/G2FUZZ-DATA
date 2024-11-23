import numpy as np

# Define the text content to be saved in the TGA file
text_content = "8. Cross-Platform Compatibility: TGA files are widely supported across different platforms and software applications."

# Create a TGA file
def create_tga_file(file_name, text_content):
    with open(file_name, 'wb') as f:
        # Header of a TGA file (18 bytes)
        header = bytearray([0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Write the header to the file
        f.write(header)

        # Write the text content to the file
        f.write(text_content.encode())

# Save the text content in a TGA file
file_name = "./tmp/cross_platform_compatibility.tga"
create_tga_file(file_name, text_content)

print(f"File '{file_name}' created successfully.")