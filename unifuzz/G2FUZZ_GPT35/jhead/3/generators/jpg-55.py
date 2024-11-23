import os
import uuid

# Define the root directory to save jpg files
root_dir = './tmp/'

# Create nested directories to represent complex file structure
complex_structure = ['images', '2022', 'January']

for directory in complex_structure:
    root_dir = os.path.join(root_dir, directory)
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

# Generate unique filename for jpg file
file_name = str(uuid.uuid4())[:8] + '.jpg'
file_path = os.path.join(root_dir, file_name)

# Save the generated jpg file
with open(file_path, 'w') as file:
    file.write('Sample JPG content')

print(f'JPG file saved at: {file_path}')