import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate pixdata files with color space information
color_space_info = "RGB"
file_content = f"Color space information: {color_space_info}"

for i in range(3):
    filename = f'./tmp/pixdata_{i}.txt'
    with open(filename, 'w') as file:
        file.write(file_content)

print("Files saved successfully in ./tmp/ directory.")