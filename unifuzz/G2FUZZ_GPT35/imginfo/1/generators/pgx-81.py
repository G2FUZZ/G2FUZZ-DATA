import os
import random
import string

def generate_random_data(size):
    data = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    return data

# Create a directory if it doesn't exist
os.makedirs('tmp', exist_ok=True)

# Generate 3 'pgx' files with random sizes and data
for i in range(3):
    file_size = (i+1) * 1000  # Simulating different file sizes incrementally
    file_name = f'./tmp/file_{i}.pgx'
    
    # Save the file with the specified size and random data
    with open(file_name, 'w') as file:
        file.write(f"File size: {file_size} KB\n")
        file.write("Random Data:\n")
        random_data = generate_random_data(file_size)
        file.write(random_data)