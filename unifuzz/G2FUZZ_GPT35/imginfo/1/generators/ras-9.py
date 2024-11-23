import os

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the feature
features = "9. Lossless Compression: 'ras' files may use lossless compression techniques to maintain image quality."

# Save the generated files into the specified directory
for i in range(5):
    filename = f'./tmp/file_{i}.ras'
    with open(filename, 'w') as file:
        file.write(features)