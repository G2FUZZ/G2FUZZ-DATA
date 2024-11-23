import os

# Define the directory to save the generated files
output_dir = './tmp/'

# Define the file name and content for the RAS file
file_name = 'complex_file.ras'
file_content = """
# Header section
FileType: Raster Dataset
DatasetName: ComplexRaster
# End of Header

# Layer 1
Layer: Layer1
Height: 100
Width: 100
DataType: Float32
# Add more attributes here for Layer1

# Layer 2
Layer: Layer2
Height: 100
Width: 100
DataType: Int16
# Add more attributes here for Layer2

# Additional layers and attributes can be added here
"""

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Write the RAS file with the complex file structure
with open(os.path.join(output_dir, file_name), 'w') as file:
    file.write(file_content)

print(f"Complex RAS file '{file_name}' with multiple layers and attributes generated in '{output_dir}'.")