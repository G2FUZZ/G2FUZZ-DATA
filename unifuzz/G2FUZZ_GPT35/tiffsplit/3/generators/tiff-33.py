from PIL import Image

# Create multiple RGBA images with varying transparency levels
image1 = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
image2 = Image.new('RGBA', (100, 100), (0, 255, 0, 200))
image3 = Image.new('RGBA', (100, 100), (0, 0, 255, 100))

# Create a new TIFF file with multiple subfiles, each with a different image
with Image.new('RGBA', (100, 100)) as master_image:
    master_image.save('./tmp/complex_tiff_file.tiff', save_all=True, append_images=[image1, image2, image3])