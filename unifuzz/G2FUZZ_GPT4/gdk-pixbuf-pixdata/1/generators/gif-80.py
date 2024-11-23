# Ensure the directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the path to the file
file_path = './tmp/example.txt'

# Write text to the file
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File has been saved to {file_path}')