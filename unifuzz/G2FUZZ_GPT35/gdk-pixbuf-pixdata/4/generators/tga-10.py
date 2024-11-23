import os

# Create a directory to store the generated TGA files
os.makedirs('./tmp/', exist_ok=True)

# Define the TGA versions
versions = ['TGA 1.0', 'TGA 2.0', 'TGA 2.1']

# Generate TGA files with version support
for version in versions:
    with open(f'./tmp/{version}.tga', 'w') as file:
        file.write(f'TGA file version: {version}')

print('TGA files generated successfully.')