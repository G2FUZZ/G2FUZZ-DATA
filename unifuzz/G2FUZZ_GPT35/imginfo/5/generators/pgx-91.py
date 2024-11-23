import os
import json
from datetime import datetime

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define metadata for the 'pgx' files
metadata = {
    'author': 'John Doe',
    'creation_date': str(datetime.now()),
    'tags': ['pgx', 'metadata', 'example'],
    'nested_metadata': {
        'version': '1.0',
        'description': 'Nested metadata example'
    }
}

# Define sections for the 'pgx' files
sections = [
    {
        'section_title': 'Section 1',
        'content': 'This is the content of section 1.'
    },
    {
        'section_title': 'Section 2',
        'content': 'This is the content of section 2.'
    }
]

# Generate 'pgx' files with metadata and sections
for i in range(3):
    filename = f'{directory}file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file_data = {
            'metadata': metadata,
            'sections': sections
        }
        json.dump(file_data, file, indent=4)

print('Files generated successfully!')