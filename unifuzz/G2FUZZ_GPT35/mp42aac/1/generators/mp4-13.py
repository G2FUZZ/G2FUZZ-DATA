import os

# Create a directory to store the generated 'mp4' files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample 'mp4' file with streaming support and Fast start feature
file_path = './tmp/streaming_faststart_example.mp4'
with open(file_path, 'wb') as f:
    # Adding Fast start feature by placing metadata at the beginning of the file
    f.write(b'MP4 Fast Start Feature - Metadata placed at the beginning for quick playback initiation. MP4 files are commonly used for streaming media over the internet.')

print(f"Generated 'mp4' file with Fast start feature: {file_path}")