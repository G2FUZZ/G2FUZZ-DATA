import os
import random
import string

# Function to generate random checksum
def generate_checksum():
    checksum = ''.join(random.choices(string.hexdigits, k=8))
    return checksum

# Generate 'pixdata' files with random data and checksum
num_files = 5
directory = './tmp/'

if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(num_files):
    filename = f'{directory}pixdata_{i}.txt'
    with open(filename, 'w') as file:
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        checksum = generate_checksum()
        file.write(f'Data: {data}\nChecksum: {checksum}')

print(f'{num_files} pixdata files generated and saved in {directory}')