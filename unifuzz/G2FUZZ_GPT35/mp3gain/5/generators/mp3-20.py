import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate mp3 files with different encoding and compression level options
for encoding_option in ['Joint Stereo', 'Stereo', 'Mono']:
    for compression_level in range(1, 6):  # Compression levels from 1 to 5
        file_path = f'./tmp/file_{encoding_option.replace(" ", "_")}_compression_{compression_level}.mp3'
        with open(file_path, 'w') as file:
            file.write(f'This is an mp3 file encoded with {encoding_option} option and compression level {compression_level}.')

print('Generated mp3 files with different encoding and compression level options successfully.')