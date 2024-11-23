import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with the specified feature
feature = "10. Lossless Compression: Some 'ras' files may use lossless compression techniques to preserve image quality during storage."
for i in range(3):
    with open(f'./tmp/file_{i + 1}.ras', 'w') as file:
        file.write(feature)

print("Generated 'ras' files successfully.")