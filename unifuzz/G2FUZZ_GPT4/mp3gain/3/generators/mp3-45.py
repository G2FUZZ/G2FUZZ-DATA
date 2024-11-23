import os

# Check if the directory exists
if not os.path.exists('./tmp'):
    # If not, create it
    os.makedirs('./tmp')

# Now, let's write a simple string to a file in this directory
file_path = './tmp/example_file.txt'
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

print(f'File saved to {file_path}')