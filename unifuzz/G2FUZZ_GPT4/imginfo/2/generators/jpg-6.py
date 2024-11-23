from PIL import Image, ImageOps

# Create a directory to store the output if it doesn't exist
import os
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Create a main image (for demonstration, we'll fill it with a solid color)
main_image = Image.new('RGB', (800, 600), color = 'blue')

# Create a thumbnail of the main image
thumbnail_size = (128, 128)
# Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
thumbnail = ImageOps.fit(main_image, thumbnail_size, Image.Resampling.LANCZOS)

# Embed the thumbnail into the main image's info dict
main_image.info['thumbnail'] = thumbnail

# Save the image with the embedded thumbnail
output_path = os.path.join(output_dir, 'image_with_thumbnail.jpg')
main_image.save(output_path, 'JPEG')

print(f'Image saved with an embedded thumbnail at {output_path}')