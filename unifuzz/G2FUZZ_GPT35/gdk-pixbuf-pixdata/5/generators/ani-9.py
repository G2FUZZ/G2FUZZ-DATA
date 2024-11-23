import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Define the metadata for the 'ani' files
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-10-01',
    'notes': 'This is a sample animation file.'
}

# Generate 'ani' files with the specified metadata
for i in range(3):
    file_name = f'./tmp/animation_{i}.ani'
    with open(file_name, 'w') as file:
        file.write(f'Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')
        file.write(f'Animation content for file {i} goes here...')

print("Generated 'ani' files with metadata successfully.")