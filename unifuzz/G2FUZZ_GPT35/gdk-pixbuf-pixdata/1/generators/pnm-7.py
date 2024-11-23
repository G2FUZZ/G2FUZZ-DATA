import os

# Define the content of the PNM file
pnm_content = """P3
# Simple PNM file
2 2
255
255 0 0   0 255 0
0 0 255   255 255 255
"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the PNM content to a file
with open('./tmp/simple.pnm', 'w') as file:
    file.write(pnm_content)

print("PNM file 'simple.pnm' has been generated and saved in './tmp/'.")