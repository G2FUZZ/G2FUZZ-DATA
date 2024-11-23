import os

# Create a directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate mif file content
mif_content = """
<Table>
<Column>
<ColumnTitle>
<TableCell>
<TableColumn>
<TableTitle>
<TableRow>
</Table>
"""

# Save the generated mif file
with open('./tmp/table_structure.mif', 'w') as file:
    file.write(mif_content)