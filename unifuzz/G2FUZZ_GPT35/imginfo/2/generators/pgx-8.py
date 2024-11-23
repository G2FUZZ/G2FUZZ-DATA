import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate pgx files with color profiles
for i in range(3):
    filename = f'{directory}file_{i}.pgx'
    with open(filename, 'w') as file:
        file.write("Color profile: sRGB\n")
        file.write("Color profile: Adobe RGB\n")
        file.write("Color profile: ProPhoto RGB\n")

print("Files generated successfully!")