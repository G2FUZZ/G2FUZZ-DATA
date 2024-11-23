import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'ras' file with compression features
compressed_data = b'RLE_COMPRESSED_DATA'

# Save the compressed data to a 'ras' file
with open('./tmp/sample.ras', 'wb') as file:
    file.write(compressed_data)