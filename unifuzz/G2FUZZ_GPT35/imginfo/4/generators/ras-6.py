import os

# Create a directory for storing the ras files
os.makedirs('./tmp/', exist_ok=True)

# Generate ras files with header information
header_info = "Image dimensions: 1920x1080\nColor space: RGB\nOther parameters: None"

for i in range(3):
    with open(f'./tmp/file_{i}.ras', 'w') as file:
        file.write(header_info)

print("RAS files generated successfully.")