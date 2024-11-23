import os
import json

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with metadata and multiple sections
for i in range(3):  # Generate 3 pixdata files
    filename = directory + f'pixdata_{i + 1}.txt'
    
    metadata = {
        "author": "John Doe",
        "date_created": "2022-01-01",
        "description": f"Details for pixdata file {i + 1}"
    }
    
    sections = [
        {"section_title": "Section 1", "content": "This is the content of section 1."},
        {"section_title": "Section 2", "content": "This is the content of section 2."},
        {"section_title": "Section 3", "content": "This is the content of section 3."}
    ]
    
    data = {
        "metadata": metadata,
        "sections": sections
    }
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

print("Generated pixdata files with metadata and multiple sections successfully.")