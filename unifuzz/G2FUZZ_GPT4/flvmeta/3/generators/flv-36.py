# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Example: Writing a file to ./tmp/
file_path = './tmp/example_file.txt'
with open(file_path, 'w') as file:
    file.write('This is an example of saving a file into ./tmp/ directory.')

print(f'File has been saved to {file_path}')