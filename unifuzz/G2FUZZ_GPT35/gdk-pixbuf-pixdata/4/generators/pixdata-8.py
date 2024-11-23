import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with the specified feature
for i in range(5):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write('8. Transparency: Support for alpha channel or transparency information in the image.')