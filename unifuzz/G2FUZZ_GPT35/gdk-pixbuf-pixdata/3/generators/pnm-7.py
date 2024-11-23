import os

# Define the content for the pnm file
pnm_content = """P3
# Portable: The 'pnm' format is considered portable as it can be easily transferred between different systems and applications.
1 1
255
255 255 255
"""

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the content to a pnm file
file_path = './tmp/portable.pnm'
with open(file_path, 'w') as file:
    file.write(pnm_content)

print(f"File '{file_path}' saved successfully.")