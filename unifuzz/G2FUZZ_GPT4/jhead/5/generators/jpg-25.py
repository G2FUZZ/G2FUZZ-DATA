# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Now, let's write a file into this directory
file_path = './tmp/generated_file.txt'
with open(file_path, 'w') as file:
    file.write('This is a generated file.')

print(f'File has been saved to {file_path}')