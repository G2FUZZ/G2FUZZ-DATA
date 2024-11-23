import os

# Create directory if it doesn't exist
directory = './tmp'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the given feature
feature = "Compatibility: Some 'ras' files may be compatible with multiple image editing and viewing software."

for i in range(3):
    filename = f'{directory}/file_{i}.ras'
    with open(filename, 'w') as file:
        file.write(feature)

print("Files generated successfully and saved in the './tmp/' directory.")