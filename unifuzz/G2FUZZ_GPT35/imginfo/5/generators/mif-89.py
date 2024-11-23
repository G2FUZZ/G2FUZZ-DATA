import os

# Create a directory to store the generated files
os.makedirs('./tmp/', exist_ok=True)

# Generate mif files with more complex file structures
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
        
        file.write('\nHeader:\n')
        file.write('    Text: "Header Section"\n')
        file.write('    FontSize: 12pt\n')
        file.write('    FontFamily: Arial\n')
        
        file.write('\nBody:\n')
        file.write('    Text: "Body Section"\n')
        file.write('    FontSize: 10pt\n')
        file.write('    FontFamily: Times New Roman\n')
        
        file.write('\nFooter:\n')
        file.write('    Text: "Footer Section"\n')
        file.write('    FontSize: 10pt\n')
        file.write('    FontFamily: Arial\n')
        
        file.write('\nTable:\n')
        file.write('    Rows: 3\n')
        file.write('    Columns: 4\n')
        file.write('    BorderColor: #000000\n')
        file.write('    CellPadding: 5px\n')
        file.write('    Data:\n')
        file.write('        1, 2, 3, 4\n')
        file.write('        5, 6, 7, 8\n')
        file.write('        9, 10, 11, 12\n')
        
        file.write('\nImage:\n')
        file.write('    Path: /path/to/image.jpg\n')
        file.write('    Width: 200px\n')
        file.write('    Height: 150px\n')
        
    print(f'Generated {filename}')

print('Files with more complex structures generated successfully.')