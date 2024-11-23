import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with the given feature
num_files = 5
feature = "Language Support: XMP supports multiple languages for metadata values, making it suitable for internationalization and localization purposes."

for i in range(1, num_files+1):
    filename = f"./tmp/file_{i}.xmp"
    with open(filename, 'w') as file:
        file.write(f"<x:xmpmeta>{feature}</x:xmpmeta>")

print(f"{num_files} xmp files generated and saved in './tmp/' directory.")