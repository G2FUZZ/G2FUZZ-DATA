import os

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Example: Saving a text file into ./tmp/
file_path = './tmp/example_file.txt'
content = 'This is an example content.'

try:
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved successfully at {file_path}")
except IOError as e:
    print(f"An error occurred: {e}")