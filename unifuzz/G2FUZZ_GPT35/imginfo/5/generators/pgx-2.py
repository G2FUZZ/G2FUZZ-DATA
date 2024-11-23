import gzip
import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Define the content to be stored in the 'pgx' files
content = "Compression: 'pgx' files may use compression techniques to reduce file size and optimize storage."

# Generate and save compressed 'pgx' files
filename = './tmp/compressed_file.pgx'
with gzip.open(filename, 'wt') as f:
    f.write(content)

print(f"File '{filename}' generated successfully.")