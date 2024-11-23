import os

# Create nested directories if they don't exist
os.makedirs('./tmp/images/', exist_ok=True)
os.makedirs('./tmp/photos/', exist_ok=True)

# Generate a JPG file inside the images directory
with open('./tmp/images/image1.jpg', 'w') as file:
    file.write('This is a JPG file inside the images directory\n')

# Generate a JPG file inside the photos directory
with open('./tmp/photos/photo1.jpg', 'w') as file:
    file.write('This is a JPG file inside the photos directory\n')

print("JPG files with complex file structures have been generated and saved in ./tmp/ directory.")