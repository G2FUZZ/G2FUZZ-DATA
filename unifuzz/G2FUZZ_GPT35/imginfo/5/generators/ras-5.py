import os

# Create a directory to store the generated 'ras' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with metadata information
metadata = {
    'image_dimensions': (1024, 768),
    'resolution': 300,
    'color_space': 'RGB',
    'creation_date': '2022-10-15'
}

for i in range(1, 6):
    filename = f'./tmp/file_{i}.ras'
    with open(filename, 'w') as file:
        file.write('Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')
    print(f'Generated file: {filename}')