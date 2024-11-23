import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate xmp files with the given feature
num_files = 5
feature = "Standardization: XMP is an ISO standard (ISO 16684-1:2012), providing a standardized way to manage metadata across different file types."

for i in range(num_files):
    with open(f'./tmp/file_{i}.xmp', 'w') as file:
        file.write(feature)

print(f'{num_files} xmp files generated and saved in ./tmp/')