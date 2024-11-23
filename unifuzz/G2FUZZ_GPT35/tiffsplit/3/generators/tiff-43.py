from PIL import Image, ImageDraw, ImageFont

# Create a new RGBA image with transparency
image = Image.new('RGBA', (100, 100), (255, 0, 0, 128))

# Create another RGBA image with different content
image2 = Image.new('RGBA', (100, 100), (0, 255, 0, 128))

# Create annotations for the images using a system font (Arial)
annotation_font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Image 1", fill=(255, 255, 255, 255), font=annotation_font)
draw = ImageDraw.Draw(image2)
draw.text((10, 10), "Image 2", fill=(255, 255, 255, 255), font=annotation_font)

# Create a list of images and their annotations to be saved in the TIFF file
images_to_save = [(image, "Layer 1"), (image2, "Layer 2")]

# Create a new blank RGBA image for composing the final multi-layer TIFF file
final_image = Image.new('RGBA', (100, 100), (0, 0, 0, 0))

# Compose the final image with multiple layers and annotations
for idx, (img, annotation) in enumerate(images_to_save):
    tmp_image = Image.new('RGBA', final_image.size, (0, 0, 0, 0))
    tmp_image.paste(img, (0, 0))
    draw = ImageDraw.Draw(tmp_image)
    draw.text((5, 80), annotation, fill=(255, 255, 255, 255), font=annotation_font)
    final_image = Image.alpha_composite(final_image, tmp_image)

# Save the final image as a multi-layer TIFF file with LZW compression
final_image.save('./tmp/multi_layer_tiff_complex.tiff', save_all=True, compression='tiff_lzw')