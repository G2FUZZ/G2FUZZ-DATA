import os

# Create a directory to store the 'ras' files if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

metadata = {
    'author': 'John Doe',
    'creation_date': '2022-10-01',
    'keywords': ['landscape', 'nature', 'mountains']
}

for i in range(3):  # Generate 3 'ras' files
    file_name = f'file_{i + 1}.ras'
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write('# Metadata\n')
        for key, value in metadata.items():
            if isinstance(value, list):
                value_str = ' '.join(value)
            else:
                value_str = str(value)
            file.write(f'{key}: {value_str}\n')