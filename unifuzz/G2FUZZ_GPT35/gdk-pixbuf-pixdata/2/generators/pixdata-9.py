import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pixdata files with the specified features
for i in range(3):
    filename = f'pixdata_{i}.txt'
    with open(os.path.join(directory, filename), 'w') as f:
        f.write("9. Resolution: May contain information about the resolution of the image, including width, height, and DPI.\n")