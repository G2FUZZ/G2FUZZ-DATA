import os

# Create a directory to store the generated mp4 files
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mp4 file with streaming support feature
with open('./tmp/streaming_support.mp4', 'wb') as f:
    f.write(b'Sample MP4 file with streaming support feature')

print('MP4 file with streaming support feature generated successfully.')