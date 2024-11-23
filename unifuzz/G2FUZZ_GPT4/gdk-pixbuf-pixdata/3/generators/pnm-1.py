import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the simplicity feature as a simple PNM image (PBM format for simplicity)
simplicity_image_data = """P1
# This is a simple PBM example
8 8
0 1 1 1 1 1 1 0
1 0 0 0 0 0 0 1
1 0 1 1 1 1 0 1
1 0 1 0 0 1 0 1
1 0 1 0 0 1 0 1
1 0 1 1 1 1 0 1
1 0 0 0 0 0 0 1
0 1 1 1 1 1 1 0
"""

# Save the simplicity image to a file
with open('./tmp/simplicity.pbm', 'w') as file:
    file.write(simplicity_image_data)