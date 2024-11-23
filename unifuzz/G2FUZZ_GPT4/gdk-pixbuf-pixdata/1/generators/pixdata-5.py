import json
import os
from datetime import datetime

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define a function to generate pixdata with metadata
def generate_pixdata_with_metadata(filename, metadata):
    # Define the path to save the file
    file_path = os.path.join('./tmp/', filename)
    
    # Construct the pixdata structure
    pixdata = {
        'metadata': metadata
    }
    
    # Save the pixdata to a file in JSON format
    with open(file_path, 'w') as file:
        json.dump(pixdata, file, indent=4)
        
    print(f'File saved: {file_path}')

# Metadata example
metadata = {
    'author': 'John Doe',
    'creation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'resolution': '1920x1080',
    'dimensions': {
        'width': 1920,
        'height': 1080
    }
}

# Generate a pixdata file with the specified metadata
generate_pixdata_with_metadata('example_pixdata.json', metadata)