import numpy as np

# Function to generate a pnm file with the given features
def generate_pnm_file(description, filename):
    pnm_data = f'''P1
# {description}
3 2
0 1 0
1 0 1
0 1 0
'''
    with open(f'./tmp/{filename}.pnm', 'w') as file:
        file.write(pnm_data)

# Features to include in the pnm file
description = "A family of image file formats used to store and transmit images in a portable manner."

# Generate pnm file
generate_pnm_file(description, 'image_file')

print("pnm file generated successfully!")