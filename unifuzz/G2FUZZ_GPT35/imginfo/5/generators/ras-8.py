import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the content of the 'ras' files
content = "8. Lossless: 'ras' files are typically lossless, preserving image quality without compression artifacts."

# Generate 'ras' files with the given content
for i in range(3):
    filename = f"{directory}file{i + 1}.ras"
    with open(filename, 'w') as file:
        file.write(content)

print("Generated 'ras' files successfully.")