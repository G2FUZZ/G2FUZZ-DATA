from PIL import Image

# Create a new RGBA image with transparency
image = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Create another RGBA image with different content
image2 = Image.new('RGBA', (100, 100), (0, 255, 0, 128))

# Create a list of images to be saved in the TIFF file
images_to_save = [image, image2]

# Save the images as a multi-layer TIFF file with LZW compression
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, img in enumerate(images_to_save):
        tmp_image.paste(img, (0, 0))
        tmp_image.save(f'./tmp/multi_layer_tiff_{idx}.tiff', save_all=True, compression='tiff_lzw')