# Ensure the ./tmp/ directory exists
import os

if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Path to the file
file_path = './tmp/example.txt'

# Data to be written
data = "This is a test."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File saved to {file_path}")