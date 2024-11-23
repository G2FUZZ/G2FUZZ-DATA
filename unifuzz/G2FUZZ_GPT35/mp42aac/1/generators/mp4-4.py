import os

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with streaming support
file_path = './tmp/streaming_example.mp4'
with open(file_path, 'wb') as f:
    f.write(b'MP4 Streaming Example - Streaming support: MP4 files are commonly used for streaming media over the internet.')

print(f"Generated 'mp4' file with streaming support: {file_path}")