import os

# Define the content to be written to the .pgx file
content = """Lossless and Lossy Compression:
JPEG 2000 supports both lossless and lossy compression methods. Lossless compression ensures that the original image data can be perfectly reconstructed from the compressed data, whereas lossy compression allows for smaller file sizes at the cost of some loss of quality.
"""

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the path to the new .pgx file
file_path = './tmp/compression_features.pgx'

# Write the content to the .pgx file
with open(file_path, 'w') as file:
    file.write(content)

print(f'File saved to {file_path}')