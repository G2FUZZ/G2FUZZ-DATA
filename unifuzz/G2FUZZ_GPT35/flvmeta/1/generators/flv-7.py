import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with the specified features
for i in range(5):
    filename = f'./tmp/video_{i}.flv'
    with open(filename, 'wb') as file:
        file.write(b'FLV Format - Compatibility: FLV files are commonly used for web-based video content playback.')

print('FLV files have been generated and saved in ./tmp/ directory.')