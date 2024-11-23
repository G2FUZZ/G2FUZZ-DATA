import os

# Create a directory to save the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save the pixdata files
metadata = {
    'resolution': '1920x1080',
    'date_created': '2022-01-15',
    'author': 'John Doe'
}

for i in range(5):  # Generate 5 pixdata files
    file_path = f'./tmp/pixdata_{i}.txt'
    with open(file_path, 'w') as file:
        file.write('Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')
    print(f'Generated {file_path}')

print('Files saved successfully.')