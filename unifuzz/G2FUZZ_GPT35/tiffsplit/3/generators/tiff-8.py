from PIL import Image

# Create a new blank image with resolution information
resolution = (300, 300)  # Resolution in dots per inch
image = Image.new('RGB', (800, 600), color='white')
image.info['dpi'] = resolution

# Save the image as a tiff file
image.save('./tmp/resolution_tiff.tiff')