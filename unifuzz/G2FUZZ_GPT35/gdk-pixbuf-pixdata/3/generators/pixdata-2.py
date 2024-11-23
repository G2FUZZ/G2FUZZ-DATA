import os

# Create a directory to store the pixdata files if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files
for i in range(3):  # Generate 3 pixdata files
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('Pixel data section for pixdata file {}\n'.format(i))