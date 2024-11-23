import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a sample JPG file with metadata and additional features
metadata = {
    'Camera Model': 'Nikon D850',
    'Exposure Time': '1/100 sec',
    'Aperture': 'f/4.5',
    'ISO': 400
}

image_features = {
    'Dimensions': '1920x1080',
    'Color Depth': '24-bit',
    'Resolution': '300 dpi'
}

file_path = os.path.join(tmp_dir, 'sample_extended.jpg')

# Simulating image generation with metadata and additional features
with open(file_path, 'wb') as file:
    file.write(b'Sample JPG file content')
    file.write(b'\n\nMetadata:\n')
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())
    
    file.write(b'\nAdditional Features:\n')
    for key, value in image_features.items():
        file.write(f'{key}: {value}\n'.encode())

print(f'Generated JPG file with metadata and additional features: {file_path}')