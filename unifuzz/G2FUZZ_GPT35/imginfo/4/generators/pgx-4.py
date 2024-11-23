import os

# Define metadata for the 'pgx' file
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-09-15',
    'description': 'Image file in pgx format'
}

# Create a directory to store the 'pgx' files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' file with metadata
for i in range(3):
    file_name = f'./tmp/file_{i + 1}.pgx'
    with open(file_name, 'w') as file:
        file.write('Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')

print('Files saved successfully!')