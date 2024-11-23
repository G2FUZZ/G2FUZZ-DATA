import os

# Create a directory if it doesn't exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate 'ras' files with random file sizes
file_sizes = [100, 500, 1000, 1500, 2000]  # File sizes in KB
for i, size in enumerate(file_sizes):
    file_name = f'{directory}file{i + 1}.ras'
    with open(file_name, 'wb') as file:
        # Write random binary data to the file based on the specified size
        file.write(os.urandom(size * 1024))  # Convert KB to bytes

print(f'{len(file_sizes)} "ras" files have been generated and saved in "{directory}" with varying file sizes.')