import os

# Define the PNG file signature
png_signature = b'\x89PNG\r\n\x1a\n'

# Create a directory to save the generated files if it does not exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generate and save the PNG file with the file signature
file_path = './tmp/generated_png_file.png'
with open(file_path, 'wb') as file:
    file.write(png_signature)

print(f"PNG file with file signature generated and saved at: {file_path}")