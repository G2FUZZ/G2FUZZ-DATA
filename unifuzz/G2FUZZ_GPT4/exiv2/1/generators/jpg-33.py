# Ensure the directory exists
import os

# Create the directory './tmp/' if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the file path
file_path = './tmp/example_file.txt'

# Open the file in write mode and write some content
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File has been saved to {file_path}')