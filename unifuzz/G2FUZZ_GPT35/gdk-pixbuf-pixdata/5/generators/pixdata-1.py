import os

# Create a directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate pixdata files with file header
for i in range(5):
    filename = f'tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('File header: Contains information about the file format and version.')

print('Files saved in ./tmp/')