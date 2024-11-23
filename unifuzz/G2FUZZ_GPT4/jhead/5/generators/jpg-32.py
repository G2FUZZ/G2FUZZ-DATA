# Define the content to write to the file
content = "This is some content to be saved in a file."

# Specify the path to the file within the ./tmp/ directory
file_path = './tmp/example_file.txt'

# Use a context manager to open the file and write content to it
try:
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File was successfully written to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")