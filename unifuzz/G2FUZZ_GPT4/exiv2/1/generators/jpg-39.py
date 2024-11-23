# Ensure the ./tmp/ directory exists
import os

# Create the directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file
file_path = './tmp/example.txt'

# Data to write
data = "This is an example."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print("File saved successfully in ./tmp/")