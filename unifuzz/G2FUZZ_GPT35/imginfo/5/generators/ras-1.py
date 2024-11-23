import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the specified features
features = "Format: The 'ras' file format is typically associated with Sun Raster image files."
file_names = ['file1.ras', 'file2.ras', 'file3.ras']

for file_name in file_names:
    with open(os.path.join(directory, file_name), 'w') as file:
        file.write(features)