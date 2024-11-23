import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pixdata' files for layer information
image_data = {
    'image1': {
        'layers': [
            {'name': 'Background', 'opacity': 1.0},
            {'name': 'Foreground', 'opacity': 0.8},
        ]
    },
    'image2': {
        'layers': [
            {'name': 'Layer1', 'opacity': 0.5},
            {'name': 'Layer2', 'opacity': 0.7},
            {'name': 'Layer3', 'opacity': 0.9},
        ]
    }
}

for image_name, data in image_data.items():
    file_path = f'./tmp/{image_name}_pixdata.txt'
    with open(file_path, 'w') as file:
        file.write(f'Layer information for {image_name}:\n')
        for i, layer in enumerate(data['layers'], start=1):
            file.write(f'Layer {i}: {layer["name"]} (Opacity: {layer["opacity"]})\n')

print('Pixdata files generated successfully!')