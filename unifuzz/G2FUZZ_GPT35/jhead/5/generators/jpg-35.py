import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate sample JPG files with metadata and multiple versions
metadata = {
    'Camera Model': 'Canon EOS Rebel',
    'Exposure Time': '1/200 sec',
    'Aperture': 'f/2.8',
    'ISO': 200
}

file_prefix = 'image_'
num_versions = 3

for i in range(1, num_versions + 1):
    file_path = os.path.join(tmp_dir, f'{file_prefix}{i}.jpg')

    # Simulating image generation with metadata for each version
    with open(file_path, 'wb') as file:
        file.write(f'Image Version {i}\n'.encode())
        file.write(b'Sample JPG file content\n')
        file.write(b'\nMetadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n'.encode())
        file.write(b'\nComments:\n')
        file.write(b'Beautiful landscape\n')

print(f'Generated {num_versions} JPG files with metadata in {tmp_dir}')