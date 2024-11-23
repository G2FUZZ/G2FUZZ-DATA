import os

# Create a directory if it does not exist
os.makedirs('./tmp/', exist_ok=True)

# Generate mif files with embedded graphics
for i in range(3):
    filename = f'./tmp/file_{i}.mif'
    with open(filename, 'w') as file:
        file.write(f'File {i} with embedded graphics')
        # Embed graphics within the document
        file.write('\nEmbedded Graphics: <img src="image.png">')  # Placeholder for embedding graphics

print('Generated mif files with embedded graphics.')