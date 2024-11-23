import os

# Create a directory to store the generated mif files
os.makedirs('./tmp/', exist_ok=True)

# Metadata information for the mif files
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-01-01',
    'document_properties': {
        'title': 'Sample Document',
        'description': 'This is a sample MIF file with metadata.'
    }
}

# Generate mif files with metadata
for i in range(3):
    filename = f'./tmp/document_{i}.mif'
    with open(filename, 'w') as f:
        f.write(f'; Metadata\n')
        f.write(f'; Author: {metadata["author"]}\n')
        f.write(f'; Creation Date: {metadata["creation_date"]}\n')
        f.write(f'; Document Properties:\n')
        for key, value in metadata["document_properties"].items():
            f.write(f'; {key}: {value}\n')
        f.write(f'\n')
        f.write(f'; Content of the document goes here...\n')

print('MIF files with metadata generated successfully.')