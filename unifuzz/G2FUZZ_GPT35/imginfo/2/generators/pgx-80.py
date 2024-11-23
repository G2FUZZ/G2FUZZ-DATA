import os
import json

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with complex file structures
for i in range(3):
    filename = f'./tmp/file_{i}.pgx'
    
    # Define a complex file structure with multiple sections and metadata
    file_structure = {
        "header": {
            "title": f"PGX File {i}",
            "author": "Anonymous",
            "created_at": "2022-10-10"
        },
        "sections": [
            {
                "title": "Section 1",
                "content": "This is the content of section 1."
            },
            {
                "title": "Section 2",
                "content": "This is the content of section 2."
            }
        ]
    }
    
    with open(filename, 'w') as file:
        json.dump(file_structure, file, indent=4)

print("Generated 'pgx' files with complex file structures successfully.")