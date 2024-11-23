from PIL import Image

# Create a new RGBA image with multiple layers (R, G, B) and different transparency levels
img = Image.new('RGBA', (200, 200), (255, 0, 0, 128))  # Red color with 50% transparency

# Create separate image bands for each color channel
r_band = Image.new('L', (200, 200), 255)  # Red channel
g_band = Image.new('L', (200, 200), 0)    # Green channel
b_band = Image.new('L', (200, 200), 0)    # Blue channel

# Split the RGBA image into its separate bands
r, g, b, a = img.split()

# Merge the separate bands into a new RGBA image
new_img = Image.merge('RGBA', (r, g, b, a))

# Create a new TIFF file with multiple layers and channels
new_img.save('./tmp/complex_image.tiff', format='TIFF')