import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the ani files with transparency
ani_files = ['file1.ani', 'file2.ani']

for file_name in ani_files:
    with open(f'./tmp/{file_name}', 'w') as file:
        file.write('Transparency: Supported')

print('ANI files generated successfully.')