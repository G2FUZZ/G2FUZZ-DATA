import os

# Create a directory tree with subdirectories
os.makedirs('./tmp/images/', exist_ok=True)
os.makedirs('./tmp/documents/', exist_ok=True)

# Generate multiple jpg files in different subdirectories
with open('./tmp/images/image1.jpg', 'w') as file:
    file.write('Content of Image 1')

with open('./tmp/images/image2.jpg', 'w') as file:
    file.write('Content of Image 2')

with open('./tmp/documents/document1.jpg', 'w') as file:
    file.write('Content of Document 1')

print('JPG files generated successfully in complex file structures!')