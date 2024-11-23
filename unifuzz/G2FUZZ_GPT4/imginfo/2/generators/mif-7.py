import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Define the content of the MIF file including styling information
mif_content = """
Version 300
Charset "WindowsLatin1"
Delimiter ","
CoordSys Earth Projection 1, 0
Columns 2
  ID Integer
  Name Char(50)
Data

  Pen (1,2,0)  /* Pen style for styling: 1 pixel, pattern 2 (solid), color 0 (black) */
  Brush (2,0,16711680)  /* Brush style for styling: pattern 2, background color 0 (transparent), foreground color 16711680 (red) */
  
Point 10 10   /* Coordinate for the Point feature */
  Symbol (35,0,12)  /* Symbol style for styling: shape 35 (circle), color 0 (black), size 12 */
  
Pline 3   /* Start of a Polyline feature definition */
  Line 15 15 20 20   /* First segment of the polyline */
  Line 20 20 25 15   /* Second segment of the polyline */
  
Region 1   /* Start of a Region feature definition */
  5   /* Number of points in the region */
    30 10
    35 15
    35 20
    30 25
    25 20
    25 15
    30 10   /* Last point, should close the region */
"""

# Save the content to a MIF file
mif_file_path = os.path.join(output_dir, 'example.mif')
with open(mif_file_path, 'w') as mif_file:
    mif_file.write(mif_content.strip())

print(f'MIF file saved to: {mif_file_path}')