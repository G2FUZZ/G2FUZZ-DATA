import os
import datetime

# Features for the pixdata files with additional complexity
features = [
    {
        "title": "Software compatibility",
        "description": "Certain 'pixdata' files may be associated with particular software programs for viewing and editing.",
        "file_size": "2 MB",
        "creation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "author": "John Doe"
    },
    {
        "title": "Resolution",
        "description": "High-resolution images suitable for printing.",
        "file_size": "5 MB",
        "creation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "author": "Jane Smith"
    }
]

# Create tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate and save pixdata files with additional complex features
for i, feature in enumerate(features):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write(f"Title: {feature['title']}\n")
        file.write(f"Description: {feature['description']}\n")
        file.write(f"File Size: {feature['file_size']}\n")
        file.write(f"Creation Date: {feature['creation_date']}\n")
        file.write(f"Author: {feature['author']}\n")

print('pixdata files with complex features generated and saved in ./tmp/ directory.')