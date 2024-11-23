import os
import json

# Create a directory for saving the generated files
os.makedirs('tmp', exist_ok=True)

# Generate 'pixdata' files with complex structures
for i in range(3):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        data = {
            'metadata': {
                'author': 'John Doe',
                'created_on': '2022-01-01',
                'description': 'This file contains pixdata information.',
            },
            'sections': [
                {'section_id': 1, 'content': 'Section 1 data...'},
                {'section_id': 2, 'content': 'Section 2 data...'},
                {'section_id': 3, 'content': 'Section 3 data...'}
            ]
        }
        file.write(json.dumps(data, indent=4))

print("Generated 'pixdata' files with complex structures saved in './tmp/' directory.")