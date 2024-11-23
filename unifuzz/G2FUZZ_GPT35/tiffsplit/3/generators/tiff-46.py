from PIL import Image, ImageDraw, ImageFont

# Define the image sizes and colors for each layer
layer_data = [
    {'size': (200, 200), 'color': (255, 0, 0, 128)},  # Layer 1
    {'size': (150, 150), 'color': (0, 255, 0, 128)},  # Layer 2
    {'size': (100, 100), 'color': (0, 0, 255, 128)}   # Layer 3
]

# Create a list of images to be saved in the TIFF file
images_to_save = [Image.new('RGBA', data['size'], data['color']) for data in layer_data]

# Define text annotations and font styles for each layer
annotations = ['Layer 1', 'Layer 2', 'Layer 3']
fonts = [ImageFont.load_default(), ImageFont.load_default(), ImageFont.load_default()]

# Save the images as a multi-layer TIFF file with text annotations and custom font styles
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, (img, annotation, font) in enumerate(zip(images_to_save, annotations, fonts)):
        tmp_image.paste(img, (0, 0))
        
        # Add text annotation to the layer with custom font style
        draw = ImageDraw.Draw(tmp_image)
        draw.text((10, 10), annotation, fill=(255, 255, 255, 255), font=font)
        
        tmp_image.save(f'./tmp/multi_layer_tiff_{idx}.tiff', save_all=True, compression='tiff_lzw')