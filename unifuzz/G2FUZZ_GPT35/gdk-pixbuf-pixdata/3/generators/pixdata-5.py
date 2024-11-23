import os

# Create a directory for saving the generated files
os.makedirs('tmp', exist_ok=True)

# Generate 'pixdata' files with compression
for i in range(3):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write("Compression: Some 'pixdata' files may employ compression techniques to reduce file size.")

print("Generated 'pixdata' files with compression saved in './tmp/' directory.")