import os

# Create a directory to save the generated files
os.makedirs('tmp', exist_ok=True)

# Generate the file header information
file_header = "File Format: pixdata\nVersion: 1.0"

# Save the file header to a file in the tmp directory
with open('./tmp/file_header.txt', 'w') as file:
    file.write(file_header)

print("File header generated and saved to ./tmp/file_header.txt")