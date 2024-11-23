import os

# Check if the ./tmp/ directory exists, and create it if it doesn't
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the file path
file_path = './tmp/example_file.txt'

# Write some content to the file
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File saved to {file_path}')