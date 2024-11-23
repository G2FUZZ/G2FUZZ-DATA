import os

# Create a directory for the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate and save 'ras' files with file header information
for i in range(3):  # Generate 3 'ras' files
    filename = f'./tmp/image_{i}.ras'
    with open(filename, 'w') as f:
        f.write("File Header: width=800, height=600, color_depth=24, compression=none")