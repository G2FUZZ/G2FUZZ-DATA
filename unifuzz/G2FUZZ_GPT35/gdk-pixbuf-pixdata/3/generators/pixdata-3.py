import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files
metadata = {
    'dimensions': '1920x1080',
    'color_depth': '24-bit',
    'compression': 'JPEG'
}

for i in range(5):
    with open(f'./tmp/pixdata_{i}.txt', 'w') as file:
        file.write('Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')