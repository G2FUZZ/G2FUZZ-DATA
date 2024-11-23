import zlib
import os

# Define the content to be compressed
content = b"Sample content to be compressed."

# Compress the content using zlib
compressed_content = zlib.compress(content)

# Create a directory to store the 'pgx' files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the compressed content to a 'pgx' file
file_path = os.path.join(directory, 'compressed_file.pgx')
with open(file_path, 'wb') as file:
    file.write(compressed_content)

print(f"'pgx' file saved successfully at: {file_path}")