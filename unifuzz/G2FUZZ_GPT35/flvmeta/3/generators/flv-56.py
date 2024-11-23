import os

# Create a directory named 'tmp' if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Save a generated file into the 'tmp' directory
with open('./tmp/generated_file.txt', 'w') as file:
    file.write('This is a generated file.')

print('File saved successfully in the ./tmp/ directory.')