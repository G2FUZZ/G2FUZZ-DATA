import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a sample JPG file with metadata and complex features
metadata = {
    'Camera Model': 'Nikon D850',
    'Exposure Time': '1/500 sec',
    'Aperture': 'f/4.0',
    'ISO': 400
}

image_dimensions = {
    'Width': 1920,
    'Height': 1080
}

color_depth = 24  # bits per pixel

file_path = os.path.join(tmp_dir, 'sample_complex.jpg')

# Simulating image generation with metadata and complex features
with open(file_path, 'wb') as file:
    file.write(b'Sample JPG file content')
    file.write(b'\n\nMetadata:\n')
    for key, value in metadata.items():
        file.write(f'{key}: {value}\n'.encode())
    
    file.write(b'\nImage Dimensions:\n')
    for key, value in image_dimensions.items():
        file.write(f'{key}: {value}\n'.encode())
    
    file.write(f'Color Depth: {color_depth} bits\n'.encode())

print(f'Generated JPG file with metadata and complex features: {file_path}')