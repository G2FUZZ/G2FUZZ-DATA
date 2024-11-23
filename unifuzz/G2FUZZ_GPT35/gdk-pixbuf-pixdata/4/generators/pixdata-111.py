import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with more complex file structures
for i in range(5):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('# Pixdata File\n')
        file.write(f'Section: Header\n')
        file.write('Description: This is the header section\n')
        file.write('\n')
        file.write(f'Section: ImageData\n')
        file.write('Format: PNG\n')
        file.write('Resolution: 1920x1080\n')
        file.write('\n')
        file.write(f'Section: Metadata\n')
        file.write('Author: John Doe\n')
        file.write('Date: 2022-09-15\n')
        file.write('\n')
        file.write(f'Section: Comments\n')
        file.write('Comment: This is a sample pixdata file\n')