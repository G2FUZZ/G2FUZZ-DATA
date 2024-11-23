import os

# Text content to be saved in a PGX file
content = """
Adaptability to Various Imaging Needs: While primarily designed for use with JPEG 2000, the characteristics of PGX files make them adaptable for various other imaging needs, including medical imaging, digital cinema, and archival, where quality and precision are paramount.
"""

# Ensuring the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# File path for the PGX file
file_path = './tmp/features.pgx'

# Writing the content to the PGX file
with open(file_path, 'w') as file:
    file.write(content.strip())

print(f"File saved at: {file_path}")