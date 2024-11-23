import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'pgx' files with color profiles
for i in range(3):
    filename = f'{directory}file{i + 1}.pgx'
    with open(filename, 'w') as file:
        file.write("Color Profile: sRGB\n")
        file.write("Color Profile: Adobe RGB\n")
        file.write("Color Profile: ProPhoto RGB\n")

print("Files generated successfully.")