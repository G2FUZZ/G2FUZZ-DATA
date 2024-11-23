# Ensure the directory exists
import os

# Create the directory if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file
file_path = './tmp/example_file.txt'

# Writing to the file
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File has been saved to {file_path}')