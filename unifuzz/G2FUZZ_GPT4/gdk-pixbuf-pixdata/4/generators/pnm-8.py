import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected argument name

# Define the path for the output PNM file
filename = './tmp/example.pbm'

# Define the image size and pattern
width, height = 64, 64  # Image dimensions
data = []  # To hold the image data

# Create a simple pattern
for y in range(height):
    row = []
    for x in range(width):
        if (x // 8) % 2 == (y // 8) % 2:
            row.append(1)  # White pixel
        else:
            row.append(0)  # Black pixel
    data.append(row)

# Write the PBM file
with open(filename, 'w') as f:
    # Write the header
    f.write('P1\n')  # P1 indicates a PBM file in ASCII encoding
    f.write(f'{width} {height}\n')  # Image dimensions
    
    # Write the image data
    for row in data:
        f.write(' '.join(str(pixel) for pixel in row) + '\n')

print(f'PBM file saved to {filename}')