import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the file to be saved
file_path = './tmp/example.txt'

# Data to be written to the file
data = "This is some example text that will be saved into the file."

# Writing data to the file
with open(file_path, 'w') as file:
    file.write(data)

print(f"File has been saved to {file_path}")