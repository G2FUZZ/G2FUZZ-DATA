import os

# Check if the ./tmp/ directory exists, and create it if it doesn't
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Now, you can save a file into this directory
file_path = './tmp/example_file.txt'
with open(file_path, 'w') as file:
    file.write('This is an example of saving a file into ./tmp/')