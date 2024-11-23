import os

# Define the file contents
file_contents = """
Name: ras
Features:
- File Format: Raster
- Description: A raster graphic file format primarily associated with Sun Microsystems workstations.
"""

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save the file with the defined contents
with open('./tmp/ras.txt', 'w') as file:
    file.write(file_contents)

print("File 'ras.txt' has been generated and saved in './tmp/' directory.")