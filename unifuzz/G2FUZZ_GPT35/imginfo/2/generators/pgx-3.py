import os
import json

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Metadata for the pgx files
metadata = {
    'image_dimensions': (1920, 1080),
    'color_space': 'RGB',
    'creation_date': '2022-09-15',
    'author': 'John Doe'
}

# Generate pgx files with metadata
for i in range(3):
    file_name = f'./tmp/file_{i + 1}.pgx'
    with open(file_name, 'w') as file:
        json.dump(metadata, file)

print("Generated pgx files with metadata successfully.")