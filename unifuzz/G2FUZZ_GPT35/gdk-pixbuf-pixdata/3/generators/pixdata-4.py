import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with color palette information
for i in range(3):
    file_name = f'./tmp/pixdata_{i}.txt'
    with open(file_name, 'w') as file:
        file.write('Color palette: Indexed color images may include a palette defining the colors used in the image.\n')