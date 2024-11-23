import os

# Create a directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate 3 'pgx' files with random sizes
for i in range(3):
    file_size = f'{i*1000} KB'  # Simulating different file sizes
    file_name = f'./tmp/file_{i}.pgx'
    
    # Save the file with the specified size
    with open(file_name, 'w') as file:
        file.write(f"File size: {file_size}\n")