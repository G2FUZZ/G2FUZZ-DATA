import os

# Create a temporary directory if it doesn't exist
tmp_dir = './tmp/'
os.makedirs(tmp_dir, exist_ok=True)

# Generate a sample JPG file with hierarchical metadata and multiple image layers
metadata = {
    'Camera': {
        'Model': 'Nikon D850',
        'Lens': '50mm f/1.8'
    },
    'Exposure': {
        'Time': '1/100 sec',
        'ISO': 400
    }
}

image_layers = [
    {
        'Layer_Type': 'Background',
        'Color': 'White',
        'Dimensions': '1920x1080'
    },
    {
        'Layer_Type': 'Foreground',
        'Object': 'Tree',
        'Position': 'Center'
    }
]

file_path = os.path.join(tmp_dir, 'sample_complex.jpg')

# Simulating image generation with hierarchical metadata and multiple image layers
with open(file_path, 'wb') as file:
    file.write(b'Sample JPG file content\n\n')
    
    file.write(b'Metadata:\n')
    for category, attributes in metadata.items():
        file.write(f'\n{category}:\n'.encode())
        for key, value in attributes.items():
            file.write(f'{key}: {value}\n'.encode())
    
    file.write(b'\nImage Layers:\n')
    for idx, layer in enumerate(image_layers, start=1):
        file.write(f'\nLayer {idx}:\n'.encode())
        for key, value in layer.items():
            file.write(f'{key}: {value}\n'.encode())

print(f'Generated JPG file with hierarchical metadata and multiple image layers: {file_path}')