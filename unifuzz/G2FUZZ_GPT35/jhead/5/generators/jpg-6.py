import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a JPG file with ".jpg" extension
with open('./tmp/file1.jpg', 'w') as file:
    file.write('This is a JPG file with .jpg extension\n')

# Generate a JPG file with ".jpeg" extension
with open('./tmp/file2.jpeg', 'w') as file:
    file.write('This is a JPG file with .jpeg extension\n')

print("JPG files have been generated and saved in ./tmp/ directory.")