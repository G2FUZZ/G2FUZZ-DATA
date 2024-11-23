import os

# Create a directory for storing the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with palette information
palette_info = {
    'file1.pixdata': {
        'palette_entries': ['red', 'green', 'blue']
    },
    'file2.pixdata': {
        'palette_entries': ['cyan', 'magenta', 'yellow', 'black']
    }
}

for filename, data in palette_info.items():
    with open(f'./tmp/{filename}', 'w') as file:
        file.write('Palette Information:\n')
        file.write('Palette Entries:\n')
        for entry in data['palette_entries']:
            file.write(f'- {entry}\n')

print("Generated pixdata files with palette information saved in './tmp/' directory.")