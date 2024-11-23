import os

# Create a directory to store the pgx files
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate pgx files with encryption
num_files = 5
for i in range(num_files):
    file_name = f'file_{i}.pgx'
    file_content = "Encrypted content here..."
    
    with open(os.path.join(output_dir, file_name), 'w') as file:
        file.write(file_content)

print(f'{num_files} pgx files with encryption have been generated and saved in {output_dir}')