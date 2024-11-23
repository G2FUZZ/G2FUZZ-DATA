import os

# Create a directory to store the generated 'pgx' files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate 'pgx' files with encryption feature
for i in range(3):
    file_name = f'file_{i}.pgx'
    file_path = os.path.join(output_dir, file_name)
    
    # Simulating encryption by writing dummy content to the file
    with open(file_path, 'w') as file:
        file.write(f"This is an encrypted 'pgx' file {i}")

print("Files generated successfully!")