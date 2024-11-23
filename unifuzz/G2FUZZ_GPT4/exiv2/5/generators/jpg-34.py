# Ensure the ./tmp/ directory exists
import os

if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Path to the file
file_path = './tmp/example_file.txt'

# Text to save
text_to_save = 'This is an example text.'

# Writing the text to the file
with open(file_path, 'w') as file:
    file.write(text_to_save)

print(f'File saved to {file_path}')