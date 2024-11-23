import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file to be saved
file_path = './tmp/example_file.txt'

# Data to be written to the file
data = "This is an example of saving a file to ./tmp/"

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File has been saved to {file_path}")