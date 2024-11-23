import json
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define metadata information
metadata = {
    'creation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'author': 'John Doe',
    'copyright': 'Copyright 2023 John Doe',
    'camera_settings': {
        'aperture': 'f/2.8',
        'shutter_speed': '1/1000',
        'iso': 100,
        'focal_length': '24mm'
    }
}

# Save the metadata to a 'pixdata' file
file_path = './tmp/image_metadata.pixdata'
with open(file_path, 'w') as file:
    json.dump(metadata, file)

print(f'Metadata saved to {file_path}')