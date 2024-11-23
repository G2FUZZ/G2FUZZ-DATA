import os

# Create a directory to store the generated 'pgx' files
os.makedirs('./tmp/', exist_ok=True)

# Generate 'pgx' files with varying sizes
for i in range(1, 6):
    file_size = i * 100  # Varying file size based on iteration
    file_path = f'./tmp/file_{i}.pgx'
    
    with open(file_path, 'wb') as file:
        file.write(os.urandom(file_size))

print("Files generated successfully.")