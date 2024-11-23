import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate mif files with page layout details
for i in range(1, 4):
    filename = f'./tmp/page_layout_{i}.mif'
    with open(filename, 'w') as file:
        file.write(f'; Page Layout Details for File {i}\n')
        file.write('Page:\n')
        file.write('    Size: A4\n')
        file.write('    MarginTop: 2cm\n')
        file.write('    MarginBottom: 2cm\n')
        file.write('    MarginLeft: 2cm\n')
        file.write('    MarginRight: 2cm\n')
        file.write('    Columns: 2\n')
        file.write('    ColumnGutter: 1cm\n')
    print(f'Generated {filename}')

print('Files generated successfully.')