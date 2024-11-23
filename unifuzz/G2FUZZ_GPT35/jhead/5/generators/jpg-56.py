import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a sample JPG file with metadata and image content
metadata = {
    'Camera Model': 'Nikon D850',
    'Exposure Time': '1/100 sec',
    'Aperture': 'f/4.5',
    'ISO': 400,
    'Lens': '50mm f/1.8',
    'Date': '2022-01-15'
}

image_content = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07...'
# Sample image content in binary data format

file_path = os.path.join(tmp_dir, 'complex_sample.jpg')

# Simulating image generation with metadata and content
with open(file_path, 'wb') as file:
    file.write(image_content)
    file.write(b'\n\nMetadata:\n')
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())

print(f'Generated complex JPG file with metadata and content: {file_path}')