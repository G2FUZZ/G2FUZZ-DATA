import os

# Creating a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generating example metadata
metadata = {
    'Author': 'John Doe',
    'Creation Date': '2021-10-01',
    'Keywords': ['data', 'document', 'example']
}

# Generating MIF file content with metadata
mif_content = f'''\
Title: Example MIF File
Author: {metadata['Author']}
Creation Date: {metadata['Creation Date']}
Keywords: {', '.join(metadata['Keywords'])}

// MIF file content goes here...
'''

# Saving the generated MIF file
file_path = './tmp/example.mif'
with open(file_path, 'w') as file:
    file.write(mif_content)

print(f'MIF file saved at: {file_path}')