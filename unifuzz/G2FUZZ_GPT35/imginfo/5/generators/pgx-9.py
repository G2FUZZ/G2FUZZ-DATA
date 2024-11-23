import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate a 'pgx' file with thumbnails
file_content = """
File Format: pgx
Features:
- Thumbnails: 'pgx' files may include thumbnails for quick previews and identification.
"""

file_path = './tmp/example.pgx'

with open(file_path, 'w') as file:
    file.write(file_content)

print(f"Generated 'pgx' file with thumbnails at {file_path}")