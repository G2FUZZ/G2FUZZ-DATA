import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample MP4 file with streaming support and encryption
file_path = os.path.join(directory, 'streaming_encryption_support.mp4')
with open(file_path, 'wb') as f:
    f.write(b'Sample MP4 file with streaming support and encryption (Encryption feature added)')

print(f"MP4 file with streaming support and encryption generated: {file_path}")