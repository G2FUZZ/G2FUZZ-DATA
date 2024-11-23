import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pgx' files with advanced features
for i in range(3):
    filename = f'{directory}file_{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write("Metadata:\n")
        file.write("Author: John Doe\n")
        file.write("Date Created: 2022-10-15\n\n")
        
        file.write("Color Profiles:\n")
        file.write("Color Profile 1: sRGB\n")
        file.write("Color Profile 2: Adobe RGB\n")
        file.write("Color Profile 3: ProPhoto RGB\n\n")
        
        file.write("Image Dimensions:\n")
        file.write("Width: 1920 pixels\n")
        file.write("Height: 1080 pixels\n\n")
        
        file.write("Additional Features:\n")
        file.write("Layer 1: Background\n")
        file.write("Layer 2: Foreground\n")
        file.write("Effects: Gaussian Blur\n")

print("Files with advanced features generated successfully.")