import os

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp', exist_ok=True)

# Generate the ani files with audio integration
ani_file1 = '''Animation File 1 with Audio Integration'''
ani_file2 = '''Animation File 2 with Audio Integration'''

# Save the generated ani files into ./tmp/
with open('./tmp/ani_file1.ani', 'w') as f:
    f.write(ani_file1)

with open('./tmp/ani_file2.ani', 'w') as f:
    f.write(ani_file2)