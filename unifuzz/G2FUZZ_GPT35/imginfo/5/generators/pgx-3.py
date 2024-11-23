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
    'tags': ['pgx', 'metadata', 'example']
}

# Generate 'pgx' files with metadata
for i in range(3):
    filename = f'{directory}file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        json.dump(metadata, file, indent=4)

print('Files generated successfully!')