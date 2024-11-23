# Define the path to the file within the ./tmp/ directory
file_path = './tmp/example.txt'

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Open the file for writing ('w') and create it if it doesn't exist
with open(file_path, 'w') as file:
    # Write some text to the file
    file.write('Hello, world!')

print('File has been saved to', file_path)