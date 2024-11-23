from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple RGB (uncompressed) BMP file
def create_rgb_bmp():
    # Create a new image with RGB mode
    img = Image.new('RGB', (100, 100), color='red')
    # Save the image
    img.save('./tmp/rgb_bmp.bmp')

# Theoretical example for RLE compression (not directly supported by Pillow for creation)
# One would typically need to manually encode the image data in RLE format and then use
# a BMP file structure to save it, as Pillow does not provide direct support for creating
# RLE-compressed BMP files. This is a placeholder to indicate where one would implement
# such functionality.
def create_rle_bmp():
    print("Creating an RLE-compressed BMP file is not directly supported by Pillow.")
    print("This would involve manually encoding the pixel data using RLE and then structuring")
    print("a BMP file header and data sections according to the BMP specification.")

# Placeholder for Bitfields compression - similar situation to RLE compression,
# where direct support in Pillow is not available. Bitfields is more relevant to
# how the color data is structured rather than compression to reduce file size.
def create_bitfields_bmp():
    print("Creating a BMP file with Bitfields compression (or color masks) is not")
    print("directly supported by Pillow and is relevant to 16-bit or 32-bit images.")
    print("This would involve defining the color masks and structuring the BMP file")
    print("accordingly, which is beyond the direct capabilities of Pillow.")

# Call the functions to create the BMP files
create_rgb_bmp()
# Note: The following functions are placeholders and do not generate actual files,
# as they illustrate points about the limits of direct support for these features in Pillow.
create_rle_bmp()
create_bitfields_bmp()