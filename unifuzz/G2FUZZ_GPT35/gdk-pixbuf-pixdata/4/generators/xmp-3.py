import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate xmp files with internationalization feature
for i in range(3):
    filename = f'./tmp/file_{i}.xmp'
    with open(filename, 'w') as file:
        file.write(f'Internationalization: XMP files support multiple languages for metadata values, enabling localization of metadata content. File {i}')