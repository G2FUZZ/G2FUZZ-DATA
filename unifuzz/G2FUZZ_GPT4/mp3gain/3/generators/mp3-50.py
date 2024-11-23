# Example: Writing to a file in ./tmp/

# Ensure the directory exists
import os

# Define the directory path
dir_path = './tmp/'

# Check if the directory exists, if not, create it
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Define the file path
file_path = os.path.join(dir_path, 'example_file.txt')

# Write to the file
with open(file_path, 'w') as file:
    file.write('Hello, world!')

print(f'File saved to {file_path}')