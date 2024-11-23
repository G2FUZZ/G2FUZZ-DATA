from PIL import Image, ImageDraw, ImageFont

# Create a new RGBA image with transparency
image = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Create another RGBA image with different content
image2 = Image.new('RGBA', (100, 100), (0, 255, 0, 128))

# Create a list of images to be saved in the TIFF file
images_to_save = [image, image2]

# Define text annotations for each layer
annotations = ['Layer 1', 'Layer 2']

# Save the images as a multi-layer TIFF file with LZW compression and text annotations
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, (img, annotation) in enumerate(zip(images_to_save, annotations)):
        tmp_image.paste(img, (0, 0))
        
        # Add text annotation to the layer
        draw = ImageDraw.Draw(tmp_image)
        font = ImageFont.load_default()  # Use default system font (Arial)
        draw.text((10, 10), annotation, fill=(255, 255, 255, 255), font=font)
        
        tmp_image.save(f'./tmp/multi_layer_tiff_{idx}.tiff', save_all=True, compression='tiff_lzw')