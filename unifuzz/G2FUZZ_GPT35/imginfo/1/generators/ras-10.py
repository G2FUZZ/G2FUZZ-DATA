import os

# Create a directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate 'ras' files with random sizes
for i in range(5):
    file_name = f'./tmp/file_{i}.ras'
    file_size = f'{i*100} KB'  # Simulating different file sizes
    with open(file_name, 'w') as file:
        file.write(f"File Size: {file_size}\n")