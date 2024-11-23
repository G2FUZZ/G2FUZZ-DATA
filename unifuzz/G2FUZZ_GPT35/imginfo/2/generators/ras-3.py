import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate 'ras' files with the specified features
features = "3. Color Depth: Supports 1-bit, 8-bit, and 24-bit color depths."
file_content = f"Features of ras file:\n{features}"

for i in range(3):
    filename = f"./tmp/file_{i + 1}.ras"
    with open(filename, 'w') as file:
        file.write(file_content)