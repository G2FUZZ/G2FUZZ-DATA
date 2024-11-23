from PIL import Image, ImageDraw, ImageEnhance

# Create a new image with white background
img = Image.new('RGB', (200, 200), color = 'white')

# Draw a simple red rectangle
d = ImageDraw.Draw(img)
d.rectangle([50, 50, 150, 150], fill ="red")

# Ensure the './tmp/' directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Save the original image as progressive JPEG
img.save('./tmp/progressive_example.jpg', 'JPEG', quality=80, progressive=True)

# Create multiple resolutions of the image
sizes = [(100, 100), (50, 50), (25, 25)]
images = [img] + [img.resize(size, Image.Resampling.LANCZOS) for size in sizes]

# Save the images as a multi-resolution TIFF to simulate hierarchical storage
# TIFF format supports saving multiple images in a single file
images[0].save(
    './tmp/hierarchical_example.tiff',
    save_all=True,
    append_images=images[1:],
    compression='jpeg',
    dpi=(200,200),
    quality=80
)