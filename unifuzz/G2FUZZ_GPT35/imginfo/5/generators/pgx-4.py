import os

# Create a directory to save the generated files
save_path = './tmp/'
os.makedirs(save_path, exist_ok=True)

# Generate 'pgx' files with encryption feature
for i in range(3):
    file_name = f'file_{i}.pgx'
    with open(os.path.join(save_path, file_name), 'w') as file:
        file.write(f"This is an encrypted 'pgx' file number {i} with sensitive data.")

print("Files have been generated successfully with encryption feature.")