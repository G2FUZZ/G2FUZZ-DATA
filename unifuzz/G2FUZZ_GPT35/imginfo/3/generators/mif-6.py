import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate a sample mif file
mif_content = """
FileHeader 0 
FileVersion 5 
FileFormat 7 
CharacterSet 2 
Language "en-US"
Tables
    Table
        Hex 1 
        TableTitle "Sample Table"
        TableWidth 4 
        TableColumn
            ColumnWidth 5
            ColumnWidth 15
            ColumnWidth 25
            ColumnWidth 35
        Row
            Cell "Header 1" 
            Cell "Header 2" 
            Cell "Header 3" 
            Cell "Header 4" 
        Row
            Cell "Data 1" 
            Cell "Data 2" 
            Cell "Data 3" 
            Cell "Data 4"
EndTable
"""
with open('./tmp/sample.mif', 'w') as f:
    f.write(mif_content)

print("MIF file generated successfully at ./tmp/sample.mif")