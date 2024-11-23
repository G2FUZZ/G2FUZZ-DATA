import os

# Create a directory for storing the generated MIF files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Document metadata for the MIF files
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-10-15',
    'document_title': 'Sample Document',
    'description': 'This is a sample MIF document.',
    'keywords': ['MIF', 'metadata', 'sample']
}

# Generate MIF files with the document metadata
for i in range(1, 4):
    filename = f'document_{i}.mif'
    with open(os.path.join(output_dir, filename), 'w') as file:
        file.write(f'; Document Metadata\n')
        for key, value in metadata.items():
            if isinstance(value, list):
                value = ', '.join(value)
            file.write(f'; {key}: {value}\n')

print("MIF files generated successfully.")