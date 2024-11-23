import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Define the path for the new file
file_path = './tmp/generated_file.txt'

# Write some content to the file
with open(file_path, 'w') as file:
    file.write('This is a generated file.')

print(f'File saved to {file_path}')