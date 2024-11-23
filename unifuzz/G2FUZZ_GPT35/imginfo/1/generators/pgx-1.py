import os

# Define the header content
header_content = """
File Format: pgx
Dimensions: 1920x1080
Color Depth: 24-bit
Compression: None
"""

# Create a directory to save the pgx files
os.makedirs('./tmp/', exist_ok=True)

# Save the header content to a pgx file
with open('./tmp/sample.pgx', 'w') as file:
    file.write(header_content)

print("File saved successfully at ./tmp/sample.pgx")