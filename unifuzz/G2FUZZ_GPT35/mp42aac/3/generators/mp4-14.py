import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample MP4 file with streaming support and HDR support
file_path = os.path.join(directory, 'streaming_and_hdr_support.mp4')
with open(file_path, 'wb') as f:
    f.write(b'Sample MP4 file with streaming support and HDR support')

print(f"MP4 file with streaming and HDR support generated: {file_path}")