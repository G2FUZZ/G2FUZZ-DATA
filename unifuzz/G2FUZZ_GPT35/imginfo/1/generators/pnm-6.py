import os

# Create a directory for storing PNM files
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the content for the PNM file
content = """P3
# Platform Independence: PNM files are platform-independent and can be easily read and written by different image processing applications.
2 2
255
255 0 0 0 255 255
0 255 0 255 0 255
"""

# Save the PNM file
file_path = os.path.join(directory, 'platform_independence.pnm')
with open(file_path, 'w') as file:
    file.write(content)

print(f'PNM file saved at: {file_path}')