from PIL import Image, ImageDraw, ImageFont

# Define the image sizes, colors, blending modes, and transparency for each layer
layer_data = [
    {'size': (200, 200), 'color': (255, 0, 0, 128), 'blend_mode': 'multiply', 'transparency': 0.5},  # Layer 1
    {'size': (200, 200), 'color': (0, 255, 0, 128), 'blend_mode': 'screen', 'transparency': 0.7},  # Layer 2
    {'size': (200, 200), 'color': (0, 0, 255, 128), 'blend_mode': 'overlay', 'transparency': 0.8}   # Layer 3
]

# Create a list of images to be saved in the TIFF file
images_to_save = [Image.new('RGBA', data['size'], data['color']) for data in layer_data]

# Define text annotations and font styles for each layer
annotations = ['Layer 1', 'Layer 2', 'Layer 3']
fonts = [ImageFont.load_default(), ImageFont.load_default(), ImageFont.load_default()]

# Save the images as a multi-layer TIFF file with text annotations, blend modes, and transparency effects
with Image.new('RGBA', (1, 1)) as tmp_image:
    for idx, (img, annotation, font, blend_mode, transparency) in enumerate(zip(images_to_save, annotations, fonts, [data['blend_mode'] for data in layer_data], [data['transparency'] for data in layer_data])):
        tmp_image.paste(img, (0, 0))
        
        # Apply blend mode to the layer
        tmp_image = Image.alpha_composite(Image.new('RGBA', tmp_image.size), tmp_image)
        tmp_image = tmp_image.convert('RGB')
        tmp_image = tmp_image.convert('RGBA')
        
        # Add transparency effect to the layer
        tmp_image.putalpha(int(255 * transparency))
        
        # Add text annotation to the layer with custom font style
        draw = ImageDraw.Draw(tmp_image)
        draw.text((10, 10), annotation, fill=(255, 255, 255, 255), font=font)
        
        tmp_image.save(f'./tmp/multi_layer_tiff_{idx}.tiff', save_all=True, compression='tiff_lzw')