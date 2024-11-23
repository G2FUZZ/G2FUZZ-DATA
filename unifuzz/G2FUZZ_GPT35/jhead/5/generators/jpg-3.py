import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a sample JPG file with metadata
metadata = {
    'Camera Model': 'Canon EOS Rebel',
    'Exposure Time': '1/200 sec',
    'Aperture': 'f/2.8',
    'ISO': 200
}

file_path = os.path.join(tmp_dir, 'sample.jpg')

# Simulating image generation with metadata
with open(file_path, 'wb') as file:
    file.write(b'Sample JPG file content')
    file.write(b'\n\nMetadata:\n')
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())

print(f'Generated JPG file with metadata: {file_path}')