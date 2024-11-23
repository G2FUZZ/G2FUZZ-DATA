import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file
with open('./tmp/generated_file.jpg', 'w') as file:
    file.write('This is a generated JPG file!')

print('JPG file generated successfully!')