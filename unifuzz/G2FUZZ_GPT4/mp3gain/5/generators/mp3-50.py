# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file
file_path = './tmp/example.txt'

# Write text to the file
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File saved to {file_path}')