import os

# Create a directory to save the generated MIF files
os.makedirs('./tmp', exist_ok=True)

# Generate MIF files with versioning
for version in range(1, 4):
    with open(f'./tmp/file_v{version}.mif', 'w') as file:
        file.write(f'MIF Version {version}\n')
        file.write('Supported Features:\n')
        file.write('- Feature 1\n')
        file.write('- Feature 2\n')
        file.write('- Feature 3\n')