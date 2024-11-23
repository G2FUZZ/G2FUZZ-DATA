import os

# Metadata information
metadata = {
    'creation_date': '2022-01-15',
    'author': 'John Doe',
    'color_profile': 'sRGB'
}

# Generate ras files with metadata
for i in range(3):
    filename = f'./tmp/file_{i+1}.ras'
    with open(filename, 'w') as file:
        file.write('Metadata:\n')
        for key, value in metadata.items():
            file.write(f'{key}: {value}\n')

print('Files generated successfully.')