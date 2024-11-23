import os

# Text to be written to the PGX file
text_content = """
6. **Scalability**: They support scalability in several dimensions, including quality, resolution, and spatial scalability. 
This enables users to extract different versions of an image from a single compressed file, catering to various application requirements without needing multiple files.
"""

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the new PGX file
file_path = './tmp/features.pgx'

# Writing the text to the PGX file
with open(file_path, 'w') as file:
    file.write(text_content)

print(f"File saved at: {file_path}")