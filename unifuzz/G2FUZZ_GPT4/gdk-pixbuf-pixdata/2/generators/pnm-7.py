import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the PNM file to demonstrate the cross-platform feature
# Here we'll create a simple PBM (Portable Bitmap) file, which is part of the PNM file family
# and represents an image in the simplest form: black and white pixels.

pbm_content = """
P1
# This is a simple example of a PBM file showing a cross (+)
5 5
0 0 0 0 0
0 0 1 0 0
0 1 1 1 0
0 0 1 0 0
0 0 0 0 0
""".strip()

# Save the PBM content to a file
pbm_file_path = './tmp/cross_platform_example.pbm'
with open(pbm_file_path, 'w') as file:
    file.write(pbm_content)

print(f"File saved to {pbm_file_path}")