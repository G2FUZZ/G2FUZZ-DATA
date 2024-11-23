from PIL import Image, ImageDraw, ImageFont, ImageChops

# Create a new image with custom color palette
color_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
data_custom_palette = [val for color in color_palette for val in color]
image_custom_palette = Image.new('P', (256, 256))
image_custom_palette.putpalette(data_custom_palette)

# Create a new image for layer3 with a different color palette
data_layer3_custom_palette = [0, 1, 2] * 256
image_layer3 = Image.new('P', (256, 256))
flat_color_palette = [val for rgb in color_palette for val in rgb]
image_layer3.putpalette(flat_color_palette)
image_layer3.putdata(data_layer3_custom_palette)

# Apply blending mode (e.g., multiply) to combine the layers
blend_image = ImageChops.multiply(image_custom_palette, image_layer3)

# Add annotations to the image
draw = ImageDraw.Draw(blend_image)
font = ImageFont.load_default()
draw.text((100, 100), "Complex TIFF Image with Custom Palette", fill=(255, 255, 255), font=font)

# Add extended metadata to the image
extended_metadata = {
    'Author': 'John Doe',
    'Resolution': (300, 300),
    'Keywords': ['complex', 'tiff', 'image', 'custom', 'palette']
}

# Save the image with extended metadata and annotations
blend_image.info.update(extended_metadata)
blend_image.save('./tmp/image_complex_extended_custom.tiff', compression='tiff_adobe_deflate')

print("A TIFF file with multiple layers, custom color palette, blending mode, annotations, and extended metadata has been saved as 'image_complex_extended_custom.tiff'.")