# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the file path
file_path = './tmp/example_file.txt'

# Write a string to the file
with open(file_path, 'w') as file:
    file.write('This is a test string.')

print(f'File has been saved to {file_path}')