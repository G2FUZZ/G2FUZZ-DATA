# Ensure the directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Example: Saving a text file into ./tmp/
file_path = './tmp/example_file.txt'
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File saved to {file_path}')