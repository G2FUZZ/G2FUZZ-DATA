import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pgx files with varying sizes
file_sizes = [1000, 5000, 10000, 20000]  # Define the sizes in bytes

for size in file_sizes:
    with open(f'./tmp/file_{size}.pgx', 'wb') as f:
        f.write(os.urandom(size))