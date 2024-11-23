import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate ras files with image data
for i in range(3):
    file_name = f'{directory}image_data_{i}.ras'
    with open(file_name, 'w') as file:
        file.write('This file contains image data.')

print('Files generated successfully.')