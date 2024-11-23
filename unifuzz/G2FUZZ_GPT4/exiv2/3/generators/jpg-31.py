# Ensure the directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the file path
file_path = './tmp/example_file.txt'

# Write a simple text file
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File has been saved to {file_path}')