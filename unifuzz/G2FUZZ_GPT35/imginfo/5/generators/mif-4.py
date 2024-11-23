import os

# Create a directory to store the generated MIF files
output_directory = './tmp/'
os.makedirs(output_directory, exist_ok=True)

# Generate MIF files with text formatting instructions
mif_file_1 = """
<document>
    <text>
        <font style="bold" size="12" color="red">Bold Red Text</font>
        <font style="italic" size="10" color="blue">Italic Blue Text</font>
        <font size="14" color="green">Large Green Text</font>
    </text>
</document>
"""

mif_file_2 = """
<document>
    <text>
        <alignment type="center">Center Aligned Text</alignment>
        <spacing before="10" after="5">Text with Spacing</spacing>
    </text>
</document>
"""

# Save the generated MIF files
with open(os.path.join(output_directory, 'text_formatting_1.mif'), 'w') as file:
    file.write(mif_file_1)

with open(os.path.join(output_directory, 'text_formatting_2.mif'), 'w') as file:
    file.write(mif_file_2)