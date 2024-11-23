# Ensure the directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Path to the file
file_path = './tmp/example.txt'

# Writing to the file
with open(file_path, 'w') as file:
    file.write('Hello, world!')