# Example Python code to save a file to ./tmp/ directory

import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file within the ./tmp/ directory
file_path = './tmp/example_file.txt'

# Writing a simple message to the file
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File has been saved to {file_path}')