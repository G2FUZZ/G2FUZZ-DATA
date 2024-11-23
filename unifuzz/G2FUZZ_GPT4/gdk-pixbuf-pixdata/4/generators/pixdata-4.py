import os
import json

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the resolution information
resolution_info = {
    "dpi": 300,
    "width_pixels": 1920,
    "height_pixels": 1080,
    "description": "High resolution image suitable for printing and high-quality display."
}

# Save the resolution information into a pixdata file
file_path = './tmp/resolution_info.pixdata'
with open(file_path, 'w') as file:
    json.dump(resolution_info, file)

print(f'Resolution information saved in {file_path}')