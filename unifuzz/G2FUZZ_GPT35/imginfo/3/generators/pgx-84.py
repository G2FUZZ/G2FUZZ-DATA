import os

# Create a directory named 'tmp' in the current directory
os.makedirs('./tmp', exist_ok=True)

# Generate a file and save it into the 'tmp' directory
file_path = './tmp/generated_file.txt'
with open(file_path, 'w') as file:
    file.write('This is a generated file.')

print('File saved at:', file_path)