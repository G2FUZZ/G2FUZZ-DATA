import os

# Define the text to be saved in the .ras file
text_content = """
6. Portability: Despite its association with Sun systems, the simplicity and versatility of the format allow for easy porting to other systems and use in cross-platform applications.
"""

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)  # Corrected the argument here

# Define the path of the file to be created
file_path = './tmp/features.ras'

# Write the text to the file
with open(file_path, 'w') as file:
    file.write(text_content)