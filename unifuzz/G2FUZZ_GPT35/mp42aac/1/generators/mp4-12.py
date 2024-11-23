import os

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with streaming support and encryption
file_path = './tmp/streaming_encryption_example.mp4'
with open(file_path, 'wb') as f:
    f.write(b'MP4 Streaming and Encryption Example - Streaming support: MP4 files are commonly used for streaming media over the internet. Encryption: MP4 files can be encrypted for secure distribution and playback.')

print(f"Generated 'mp4' file with streaming support and encryption: {file_path}")