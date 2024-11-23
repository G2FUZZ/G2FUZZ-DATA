import os
import json

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with color palette information and metadata
for i in range(3):
    file_name = f'./tmp/pixdata_{i}.txt'
    metadata = {
        'image_name': f'image_{i}.png',
        'resolution': '1024x768',
        'created_by': 'Pixdata Generator'
    }
    with open(file_name, 'w') as file:
        file.write('Color palette: Indexed color images may include a palette defining the colors used in the image.\n')
        file.write('\nMetadata:\n')
        file.write(json.dumps(metadata, indent=4))