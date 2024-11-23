import os

# Create a directory to save the generated mp3 files
os.makedirs('./tmp/', exist_ok=True)

# Generate mp3 files with different encoding options
for encoding_option in ['Joint Stereo', 'Stereo', 'Mono', 'DRM Protected']:
    if encoding_option == 'DRM Protected':
        file_path = f'./tmp/file_{encoding_option.replace(" ", "_")}.mp3'
        with open(file_path, 'w') as file:
            file.write('This is an mp3 file with DRM Protection.')
    else:
        file_path = f'./tmp/file_{encoding_option.replace(" ", "_")}.mp3'
        with open(file_path, 'w') as file:
            file.write(f'This is an mp3 file encoded with {encoding_option} option.')

print('Generated mp3 files with different encoding options successfully.')