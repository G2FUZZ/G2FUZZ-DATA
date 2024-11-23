import os

# Define the content for the pnm file
content = """P3
# Flexibility: PNM files support various image resolutions and can be easily manipulated for different display purposes.
1 1
255
255 0 0
"""

# Create a directory if it does not exist
directory = './tmp/'
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the content to a pnm file in the tmp directory
with open('./tmp/flexibility.pnm', 'w') as file:
    file.write(content)

print("Flexibility feature saved in ./tmp/flexibility.pnm")