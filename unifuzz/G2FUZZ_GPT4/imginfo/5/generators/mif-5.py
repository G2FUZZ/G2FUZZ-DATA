import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# The path to the MIF file to be created
mif_file_path = './tmp/example.mif'

# MIF content with conditional text
mif_content = """
<MIFFile 9.00> # Start of the MIF file with version
# Define Conditional Text Settings
<Conditional <CTag `Audience1`> <CState `Show`>>
<Conditional <CTag `Audience2`> <CState `Hide`>>

# Beginning of the content
<PgfTag `Body`> # Paragraph tag, assuming definition elsewhere
<ParaLine
  <String `This is visible to all audiences.`>
> # End ParaLine
<ParaLine
  <CondText
    <CTag `Audience1`>
    <String `This content is specifically for Audience 1.`>
  >
> # End ParaLine
<ParaLine
  <CondText
    <CTag `Audience2`>
    <String `This content is specifically for Audience 2.`>
  >
> # End ParaLine
<ParaLine
  <String `General information relevant to all audiences.`>
> # End ParaLine
# End of the content

<Trail MIFFile> # End of the MIF file
"""

# Write the content to the MIF file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content)

print(f'MIF file with conditional text has been created at {mif_file_path}')