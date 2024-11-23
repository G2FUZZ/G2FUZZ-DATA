import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with file headers
num_files = 5

for i in range(num_files):
    file_name = f'./tmp/file_{i+1}.ras'
    with open(file_name, 'w') as file:
        file.write("Image Dimensions: 1920x1080\n")
        file.write("Color Depth: 24-bit\n")
        file.write("Compression Method: None\n")
        file.write("Other Properties: ...\n")

print(f"{num_files} 'ras' files generated and saved in './tmp/' directory.")