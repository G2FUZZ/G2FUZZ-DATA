# Define the path to the file you want to create
file_path = './tmp/example.txt'

# Ensure the directory exists (create it if it doesn't)
import os
if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))

# Write some content to the file
with open(file_path, 'w') as file:
    file.write('This is an example of saving a file to the ./tmp/ directory.')

print(f'File has been saved to {file_path}')