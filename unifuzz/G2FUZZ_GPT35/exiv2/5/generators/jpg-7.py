import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate a sample JPEG file
file_path = os.path.join(directory, 'example.jpg')
with open(file_path, 'wb') as file:
    file.write(b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xED\x00\x1CPhotoshop 3.0\x008BIM\x04\x04\x00\x00\x00\x00\x00\x00\x80\x1C\x02\x03\x01\x08\x00')