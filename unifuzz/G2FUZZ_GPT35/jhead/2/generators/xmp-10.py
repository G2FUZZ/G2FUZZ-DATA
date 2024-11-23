import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with the provided feature
num_files = 5
feature = "Standardization: XMP is an open standard maintained by Adobe and supported by various software vendors, ensuring consistency and compatibility in metadata handling."

for i in range(num_files):
    filename = f'{directory}/file_{i}.xmp'
    with open(filename, 'w') as file:
        file.write(feature)