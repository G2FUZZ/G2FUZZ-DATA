import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Path to the new .mif file
mif_file_path = './tmp/font_color_info.mif'

# MIF content with font and color information
mif_content = """
<MIFFile 9.00> # MIF version
<FontCatalog
 <Font
  <FTag `BodyText`>
  <FFamily `Times New Roman`>
  <FVar `Regular`>
  <FWeight `Medium`>
  <FAngle `Regular`>
  <FSize 12.0>
  <FColor `Black`>>
 <Font
  <FTag `Heading1`>
  <FFamily `Arial`>
  <FVar `Regular`>
  <FWeight `Bold`>
  <FAngle `Regular`>
  <FSize 24.0>
  <FColor `Blue`>>
> # End of FontCatalog
<ColorCatalog
 <Color
  <ColorTag `Black`>
  <ColorCyan 0>
  <ColorMagenta 0>
  <ColorYellow 0>
  <ColorBlack 100>>
 <Color
  <ColorTag `Blue`>
  <ColorCyan 100>
  <ColorMagenta 50>
  <ColorYellow 0>
  <ColorBlack 0>>
> # End of ColorCatalog
"""

# Write the MIF content to the file
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content.strip())

print(f'MIF file created at: {mif_file_path}')