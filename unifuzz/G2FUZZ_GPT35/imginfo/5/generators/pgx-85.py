import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pgx' files with complex file structures
for i in range(3):
    filename = f'{directory}file{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write("=== File Information ===\n")
        file.write("Filename: file{i + 1}.pgx\n")
        file.write("Author: John Doe\n")
        file.write("\n")
        file.write("=== Color Profiles ===\n")
        file.write("Color Profile 1: sRGB\n")
        file.write("Color Profile 2: Adobe RGB\n")
        file.write("Color Profile 3: ProPhoto RGB\n")
        file.write("\n")
        file.write("=== Metadata ===\n")
        file.write("Date Created: 2022-01-01\n")
        file.write("Resolution: 300 dpi\n")
        file.write("Keywords: photography, design, colors\n")

print("Files with complex structures generated successfully.")