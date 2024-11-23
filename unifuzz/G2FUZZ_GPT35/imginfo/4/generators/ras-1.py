import os

# Define the content for the ras files
ras_content = "Format: The 'ras' file format is commonly used for storing raster graphics data."

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate and save 'ras' files
for i in range(3):
    file_name = f'./tmp/file_{i}.ras'
    with open(file_name, 'w') as file:
        file.write(ras_content)