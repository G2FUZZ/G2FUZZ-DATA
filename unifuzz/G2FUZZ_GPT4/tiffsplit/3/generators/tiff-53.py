from PIL import Image
import os

def create_gradient_image(width, height, gradient_color=(128,)):
    image = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            color = (int(x % 256), int(y % 256), gradient_color[0])
            image.putpixel((x, y), color)
    return image

def save_multipage_tiff_with_metadata(output_path, images, tiff_info):
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        compression='tiff_adobe_deflate',
        dpi=(300, 300)
    )

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create gradient images
images = [create_gradient_image(256, 256, gradient_color=(gc,)) for gc in (128, 64, 192)]

# Output path for the multi-page TIFF with metadata
output_path = os.path.join(output_dir, 'gradient_multipage_tiff_with_metadata.tiff')

# Save the multi-page TIFF with metadata
save_multipage_tiff_with_metadata(output_path, images, {})

print(f"Multi-page TIFF with metadata saved to {output_path}")