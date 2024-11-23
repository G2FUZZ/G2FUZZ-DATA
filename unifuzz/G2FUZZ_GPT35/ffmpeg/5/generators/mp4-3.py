import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a simple mp4 file with the specified feature
filename = './tmp/streaming_feature.mp4'

with open(filename, 'wb') as file:
    file.write(b'Generated MP4 file with streaming feature')

print(f'Generated {filename}')