import zlib
import os

# Create a directory for storing generated 'ani' files
os.makedirs('./tmp/', exist_ok=True)

# Data to be stored in the 'ani' file
data = b"Animation data to be compressed."

# Compress the data using zlib
compressed_data = zlib.compress(data)

# Save the compressed data to a file with '.ani' extension
with open('./tmp/generated_file.ani', 'wb') as file:
    file.write(compressed_data)

print("Generated 'ani' file saved successfully.")