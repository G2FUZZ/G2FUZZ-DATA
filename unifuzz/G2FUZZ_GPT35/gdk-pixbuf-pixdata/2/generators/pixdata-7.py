import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with alpha channel
for i in range(3):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('Features:\n')
        file.write('1. Resolution: 1920x1080\n')
        file.write('2. Color depth: 24-bit\n')
        file.write('3. Compression: Lossless\n')
        file.write('4. Format: PNG\n')
        file.write('5. Size: 2MB\n')
        file.write('6. Dimensions: 16:9\n')
        file.write('7. Alpha channel: Included\n')
    
    print(f'Generated {filename}')