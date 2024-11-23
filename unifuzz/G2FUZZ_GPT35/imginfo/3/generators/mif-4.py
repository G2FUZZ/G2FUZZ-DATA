import os

# Create the directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Generate the mif file
graphics_mif_content = """
Graphics File:
- Images
- Shapes
- Positioning
"""

with open('./tmp/graphics.mif', 'w') as file:
    file.write(graphics_mif_content)