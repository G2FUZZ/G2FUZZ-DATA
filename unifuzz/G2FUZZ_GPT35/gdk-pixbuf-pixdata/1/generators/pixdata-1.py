import os

# Define the file header information
file_header = """
File Format: pixdata
Version: 1.0
"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the file with the file header information
with open('./tmp/pixdata_file.txt', 'w') as file:
    file.write(file_header)

print("File generated and saved successfully.")