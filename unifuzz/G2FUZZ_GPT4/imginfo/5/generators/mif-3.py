import os

# Ensure the target directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the MIF content with page layout information
mif_content = """
<MIFFile 9.00> # MIF version
<Units Uinch> # Unit of measurement

# Define a page layout
<Page
    <PageType Start>
    <PageSize 8.5\" x 11\"> # Letter size
    <PageOrientation Portrait>
    <TextRect
        <ID 1>
        <TR_PageNum 1>
        <TR_CoordRect 0.5\" 0.5\" 7.5\" 10\"> # Margins: top, left, width, height
        <TR_Fill 15> # Fill color
        <TR_Columns 2> # Number of columns
        <TR_ColGap 0.25\"> # Gap between columns
    >
>
"""

# Save the MIF content to a file
file_path = os.path.join(output_dir, 'layout_info.mif')
with open(file_path, 'w') as file:
    file.write(mif_content.strip())

print(f'MIF file with page layout information saved to: {file_path}')