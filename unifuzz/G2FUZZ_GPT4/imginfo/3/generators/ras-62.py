# Ensure the directory exists
import os

# Create the directory './tmp/' if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the path of the file to be created within './tmp/'
file_path = './tmp/example_file.txt'

# Write some content to the file
with open(file_path, 'w') as file:
    file.write('This is a test file.')

print(f'File has been saved to {file_path}')