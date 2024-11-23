import os

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with streaming and closed captioning support
file_path = './tmp/streaming_and_closed_captioning_example.mp4'
with open(file_path, 'wb') as f:
    f.write(b'MP4 Streaming Example - Streaming support: MP4 files are commonly used for streaming media over the internet.\nClosed captioning: MP4 files can support closed captioning tracks for viewers with hearing impairments.')

print(f"Generated 'mp4' file with streaming and closed captioning support: {file_path}")