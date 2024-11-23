import os

# Define the content to be written in the 'ras' files
content = "7. Support: 'ras' files are supported by various image viewing and editing software."

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate and save 'ras' files
for i in range(3):
    file_path = os.path.join(directory, f'file_{i+1}.ras')
    with open(file_path, 'w') as file:
        file.write(content)

print("Generated 'ras' files successfully.")