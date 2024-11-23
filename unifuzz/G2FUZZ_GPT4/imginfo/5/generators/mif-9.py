import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the content of the MIF file with object anchoring
mif_content = """
# MIF example with Object Anchoring
< MIFFile 9 > # Indicates MIF format version
< Units Uinch > # Unit of measurement
< TextFlow
  < TFAutoConnect 0 >
  < TFRectID 1 >
  < TFGutter 12 pt >
  < TFColumnCount 1 >
  < TFColumnGutter 12 pt >
  < Para
    < PgfTag `BodyText` >
    < PgfPlacement Anywhere >
    < PgfSpBefore 12 pt >
    < PgfWithPrev 0 >
    < TextRectID 2 >
    < Unique 10000 >
    < ParaLine
      < String `This demonstrates object anchoring in MIF files.` >
    > # ParaLine ends
  > # Para ends
  < AnchoredFrame
    < ID 2 >
    < AFrameRect 1.0 in 1.0 in 3.0 in 2.0 in > # Position and size
    < AFrameAnchored 1 > # Anchor type to the text
    < AFrameAlignment Center > # Alignment
    < AFrameAngle 0 > # Rotation angle
    > # AnchoredFrame ends
> # TextFlow ends
"""

# Path to save the MIF file
file_path = './tmp/object_anchoring_example.mif'

# Writing the MIF content to the file
with open(file_path, 'w') as mif_file:
    mif_file.write(mif_content.strip())

print(f'MIF file with object anchoring feature has been saved to {file_path}')