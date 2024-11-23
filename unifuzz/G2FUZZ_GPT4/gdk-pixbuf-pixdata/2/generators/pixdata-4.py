import json
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Metadata information to be stored
metadata = {
    'creation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'copyright': 'Copyright 2023',
    'camera_settings': {
        'iso': 100,
        'shutter_speed': '1/125',
        'aperture': 'f/2.8'
    },
    'gps_coordinates': {
        'latitude': '51.5074 N',
        'longitude': '0.1278 W'
    }
}

# Simulate image data (in a real scenario, this would be binary image data)
image_data = {
    'width': 1920,
    'height': 1080,
    'color_mode': 'RGB'
}

# Combine image data and metadata into a single structure
pixdata = {
    'image_data': image_data,
    'metadata': metadata
}

# Save the data to a .pixdata file
file_path = './tmp/sample.pixdata'
with open(file_path, 'w') as file:
    json.dump(pixdata, file, indent=4)

print(f'Pixdata file saved to {file_path}')