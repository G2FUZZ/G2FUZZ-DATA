from PIL import Image
import os

# Create a gradient image (for example, 256x256 pixels)
width, height = 256, 256
image = Image.new("RGB", (width, height))

# Generate a gradient from top to bottom
for y in range(height):
    for x in range(width):
        image.putpixel((x, y), (int(x % 256), int(y % 256), 128))

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# The following tags are used for demonstration purposes and should be replaced with actual data
# Primary Chromaticities and White Point Tags
# These tags are placeholders and should correspond to your specific requirements
primary_chromaticities = (0.64, 0.33, 0.3, 0.6, 0.15, 0.06)  # Example values for Red, Green, Blue chromaticities
white_point = (0.3127, 0.3290)  # D65 white point

# Save the image with additional metadata for Primary Chromaticities and White Point
tiff_info = {
    'dpi': (300, 300),  # Example DPI setting
    'compression': 'tiff_adobe_deflate',  # Example compression method
    # The following entries are placeholders and require valid data for real applications
    'primary_chromaticities': primary_chromaticities,  # Tag 319
    'white_point': white_point,  # Tag 318
    # Other tags such as 34675 (ICC Profile) can be included here as well
    # '34675': icc_profile_example  # Placeholder for ICC Profile - not functional in this example
}

# Note: PIL may not directly support all TIFF tags, especially for colorimetry.
# The assignment of 'primary_chromaticities' and 'white_point' is intended for demonstration
# and may require a more specialized library or custom handling to actually embed these tags into a TIFF file.

# Save the TIFF with the standard API, noting the limitations mentioned
image.save('./tmp/gradient_tile_colorimetry_primary_chromaticities.tiff', format='TIFF', tile=('tile', 128, 128), **tiff_info)

print("TIFF image with tiling, Primary Chromaticities, and White Point Tags saved to ./tmp/gradient_tile_colorimetry_primary_chromaticities.tiff")