import os
import random

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a jpg file with File Size Variability
file_content = 'This is a generated JPG file!\n'
file_content += 'File Size Variability: {}'.format(random.randint(100, 1000))  # Generating a random file size variability

with open('./tmp/generated_file_with_variability.jpg', 'w') as file:
    file.write(file_content)

print('JPG file with File Size Variability generated successfully!')