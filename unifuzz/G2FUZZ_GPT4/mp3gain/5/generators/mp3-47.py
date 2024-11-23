import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Path to the file to be saved
file_path = './tmp/example_file.txt'

# Data to be written to the file
data = "This is a test file."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print("File saved successfully.")