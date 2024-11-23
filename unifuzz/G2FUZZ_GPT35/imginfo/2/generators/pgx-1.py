import os

# Define the file header for pgx files
file_header = "PGX FILE FORMAT\n"

# Create a directory to store the pgx files if it does not exist
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate pgx files with the specified features
num_files = 5
for i in range(num_files):
    filename = f'{output_dir}file_{i+1}.pgx'
    with open(filename, 'w') as file:
        file.write(file_header)

print(f'{num_files} pgx files generated and saved in {output_dir}')