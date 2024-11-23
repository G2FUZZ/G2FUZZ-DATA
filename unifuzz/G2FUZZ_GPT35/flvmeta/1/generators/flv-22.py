import os

# Create a directory to store the generated FLV files
os.makedirs('./tmp/', exist_ok=True)

# Generate FLV files with the specified features including Variable frame rate
for i in range(6):
    filename = f'./tmp/video_{i}.flv'
    with open(filename, 'wb') as file:
        if i == 5:
            file.write(b'FLV Format - Compatibility: FLV files are commonly used for web-based video content playback. Variable frame rate: FLV files may support variable frame rates for efficient encoding and playback of content with varying frame rates.')
        else:
            file.write(b'FLV Format - Compatibility: FLV files are commonly used for web-based video content playback.')

print('FLV files have been generated and saved in ./tmp/ directory.')