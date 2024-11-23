import os

# Create directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate mif file with metadata
metadata = {
    'author': 'John Doe',
    'creation_date': '2022-09-28',
    'document_properties': {
        'title': 'Sample Document',
        'description': 'This is a sample document with metadata.'
    }
}

mif_content = f"""
Metadata:
Author={metadata['author']}
CreationDate={metadata['creation_date']}
DocumentProperties: <<
    Title={metadata['document_properties']['title']}
    Description={metadata['document_properties']['description']}
    >>
"""

file_path = os.path.join(directory, 'sample.mif')
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f"Generated mif file with metadata at: {file_path}")