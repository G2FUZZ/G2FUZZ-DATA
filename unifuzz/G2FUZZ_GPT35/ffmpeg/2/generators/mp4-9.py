import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with the specified feature
with open('./tmp/streaming_support.mp4', 'wb') as file:
    file.write(b'MP4 file with streaming support: efficient compression and compatibility with streaming protocols.')